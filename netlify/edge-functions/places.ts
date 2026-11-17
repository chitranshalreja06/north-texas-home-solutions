// Netlify Edge Function: proxies Google Places Autocomplete API (New)
// The Google API key lives in the GOOGLE_PLACES_API_KEY env var, never in client code.
import type { Context } from "@netlify/edge-functions";

export default async (req: Request, context: Context) => {
  const url = new URL(req.url);

  // Only allow POST to /api/places-autocomplete and GET to /api/place-details
  if (req.method === "OPTIONS") {
    return new Response(null, {
      status: 204,
      headers: {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type",
      },
    });
  }

  const apiKey = Netlify.env.get("GOOGLE_PLACES_API_KEY");
  if (!apiKey) {
    return new Response(JSON.stringify({ error: "Places API not configured" }), {
      status: 500,
      headers: { "Content-Type": "application/json" },
    });
  }

  const cors = {
    "Access-Control-Allow-Origin": "*",
    "Content-Type": "application/json",
  };

  try {
    if (url.pathname === "/api/places-autocomplete" && req.method === "POST") {
      const body = await req.json();
      const input = (body.input || "").toString().trim();
      if (!input || input.length < 2) {
        return new Response(JSON.stringify({ suggestions: [] }), { headers: cors });
      }

      const res = await fetch("https://places.googleapis.com/v1/places:autocomplete", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-Goog-Api-Key": apiKey,
          "X-Goog-FieldMask": "suggestions.placePrediction.placeId,suggestions.placePrediction.text",
        },
        body: JSON.stringify({
          input,
          includedRegionCodes: ["us"],
          includeQueryPredictions: false,
        }),
      });

      if (!res.ok) {
        return new Response(JSON.stringify({ suggestions: [] }), { headers: cors });
      }

      const data = await res.json();
      const suggestions = (data.suggestions || []).map((s: any) => ({
        placeId: s.placePrediction?.placeId || "",
        text: s.placePrediction?.text?.text || "",
      })).filter((s: any) => s.placeId && s.text);

      return new Response(JSON.stringify({ suggestions }), { headers: cors });
    }

    if (url.pathname === "/api/place-details" && req.method === "GET") {
      const placeId = url.searchParams.get("placeId") || "";
      if (!placeId) {
        return new Response(JSON.stringify({ error: "Missing placeId" }), { status: 400, headers: cors });
      }

      const res = await fetch(
        `https://places.googleapis.com/v1/places/${encodeURIComponent(placeId)}`,
        {
          headers: {
            "X-Goog-Api-Key": apiKey,
            "X-Goog-FieldMask": "formattedAddress",
          },
        }
      );

      if (!res.ok) {
        return new Response(JSON.stringify({ error: "Place not found" }), { status: 404, headers: cors });
      }

      const data = await res.json();
      return new Response(JSON.stringify({ formattedAddress: data.formattedAddress || "" }), { headers: cors });
    }

    return new Response(JSON.stringify({ error: "Not found" }), { status: 404, headers: cors });
  } catch (e) {
    return new Response(JSON.stringify({ suggestions: [] }), { headers: cors });
  }
};

export const config = { path: ["/api/places-autocomplete", "/api/place-details"] };
