// Lead modal controls
function openLeadModal(){var m=document.getElementById('lead-modal');if(m){m.classList.add('open');m.setAttribute('aria-hidden','false');document.body.style.overflow='hidden';}}
function closeLeadModal(){var m=document.getElementById('lead-modal');if(m){m.classList.remove('open');m.setAttribute('aria-hidden','true');document.body.style.overflow='';}}
document.addEventListener('keydown',function(e){if(e.key==='Escape')closeLeadModal();});
function toggleOtherField(sel){var w=document.getElementById('m-other-wrap');if(w){w.style.display=sel.value==='Other'?'block':'none';}}
// Google Places address autocomplete
var GOOGLE_PLACES_KEY = "AIzaSyDzK7l0q2fWi5U8SR3GYdFFIx59c3n5z7M";
(function initAddressAutocomplete(){
  if(!GOOGLE_PLACES_KEY)return;
  function attach(input){
    if(!input||input.dataset.placesAttached)return;
    input.dataset.placesAttached="1";
    try{
      var ac=new google.maps.places.Autocomplete(input,{types:['address'],componentRestrictions:{country:'us'},fields:['formatted_address']});
      ac.addListener('place_changed',function(){var p=ac.getPlace();if(p&&p.formatted_address)input.value=p.formatted_address;});
    }catch(e){}
  }
  window.nthsInitPlaces=function(){
    document.querySelectorAll('input[name="address"]').forEach(attach);
  };
  var s=document.createElement('script');
  s.src='https://maps.googleapis.com/maps/api/js?key='+encodeURIComponent(GOOGLE_PLACES_KEY)+'&libraries=places&callback=nthsInitPlaces';
  s.async=true;s.defer=true;document.head.appendChild(s);
})();
