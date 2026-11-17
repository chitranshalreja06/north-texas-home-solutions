// Lead modal controls
function openLeadModal(){var m=document.getElementById('lead-modal');if(m){m.classList.add('open');m.setAttribute('aria-hidden','false');document.body.style.overflow='hidden';}}
function closeLeadModal(){var m=document.getElementById('lead-modal');if(m){m.classList.remove('open');m.setAttribute('aria-hidden','true');document.body.style.overflow='';}}
document.addEventListener('keydown',function(e){if(e.key==='Escape')closeLeadModal();});
function toggleOtherField(sel){var w=document.getElementById('m-other-wrap');if(w){w.style.display=sel.value==='Other'?'block':'none';}}
// Address autocomplete via Netlify Edge Function proxy (no API key in client code)
(function initAddressAutocomplete(){
  function attach(input){
    if(!input||input.dataset.placesAttached)return;
    input.dataset.placesAttached="1";
    var list=null, timer=null, items=[], activeIdx=-1;
    function closeList(){ if(list){list.remove();list=null;} activeIdx=-1; items=[]; }
    function showList(suggestions){
      closeList();
      if(!suggestions.length)return;
      list=document.createElement('div');
      list.className='nths-places-list';
      list.style.cssText='position:absolute;z-index:9999;background:#fff;border:1px solid #d0d7e3;border-radius:8px;box-shadow:0 8px 24px rgba(10,22,40,.15);max-height:240px;overflow-y:auto;margin-top:4px;left:0;right:0;';
      suggestions.forEach(function(s,i){
        var d=document.createElement('div');
        d.textContent=s.text;
        d.style.cssText='padding:10px 14px;cursor:pointer;font-size:.9rem;color:#1a2b45;border-bottom:1px solid #eef1f5;';
        d.addEventListener('mouseenter',function(){ setActive(i); });
        d.addEventListener('mousedown',function(e){ e.preventDefault(); selectItem(i); });
        list.appendChild(d);
      });
      var parent=input.parentElement;
      if(parent){ if(getComputedStyle(parent).position==='static')parent.style.position='relative'; parent.appendChild(list); }
      items=suggestions;
    }
    function setActive(i){
      activeIdx=i;
      if(!list)return;
      Array.prototype.forEach.call(list.children,function(c,idx){
        c.style.background=idx===i?'#eef2f8':'';
      });
    }
    function selectItem(i){
      var s=items[i];
      if(!s)return;
      fetch('/api/place-details?placeId='+encodeURIComponent(s.placeId))
        .then(function(r){return r.json();})
        .then(function(d){ if(d.formattedAddress)input.value=d.formattedAddress; else input.value=s.text; })
        .catch(function(){ input.value=s.text; });
      closeList();
    }
    input.addEventListener('input',function(){
      var q=input.value.trim();
      clearTimeout(timer);
      if(q.length<3){ closeList(); return; }
      timer=setTimeout(function(){
        fetch('/api/places-autocomplete',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({input:q})})
          .then(function(r){return r.json();})
          .then(function(d){ showList(d.suggestions||[]); })
          .catch(function(){ closeList(); });
      },250);
    });
    input.addEventListener('keydown',function(e){
      if(!list||!items.length)return;
      if(e.key==='ArrowDown'){ e.preventDefault(); setActive(Math.min(activeIdx+1,items.length-1)); }
      else if(e.key==='ArrowUp'){ e.preventDefault(); setActive(Math.max(activeIdx-1,0)); }
      else if(e.key==='Enter'&&activeIdx>=0){ e.preventDefault(); selectItem(activeIdx); }
      else if(e.key==='Escape'){ closeList(); }
    });
    document.addEventListener('click',function(e){
      if(list&&!list.contains(e.target)&&e.target!==input)closeList();
    });
  }
  document.querySelectorAll('input[name="address"]').forEach(attach);
})();
