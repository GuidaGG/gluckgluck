/* global CKEDITOR */
;(function() {
  var el = document.getElementById('ckeditor-init-script');
  if (el && !window.CKEDITOR_BASEPATH) {
    window.CKEDITOR_BASEPATH = el.getAttribute('data-ckeditor-basepath');
  }

  // Polyfill from https://developer.mozilla.org/en/docs/Web/API/Element/matches
  if (!Element.prototype.matches) {
    Element.prototype.matches =
        Element.prototype.matchesSelector ||
        Element.prototype.mozMatchesSelector ||
        Element.prototype.msMatchesSelector ||
        Element.prototype.oMatchesSelector ||
        Element.prototype.webkitMatchesSelector ||
        function(s) {
            var matches = (this.document || this.ownerDocument).querySelectorAll(s),
                i = matches.length;
            while (--i >= 0 && matches.item(i) !== this) {}
            return i > -1;
        };
  }

  function runInitialisers() {
    if (!window.CKEDITOR) {
     setTimeout(runInitialisers, 100);
      return;
    }

    initialiseCKEditor();
    initialiseCKEditorInInlinedForms();
  }

  if (document.readyState != 'loading' && document.body) {
    document.addEventListener('DOMContentLoaded', initialiseCKEditor);
    runInitialisers();
  } else {
    document.addEventListener('DOMContentLoaded', runInitialisers);
  }

  function initialiseCKEditor() {
    var containers = document.getElementsByClassName('inline-related ');

    for (var i=0; i<containers.length; ++i) {
    var classes = containers[i].className;

    var textareas = Array.prototype.slice.call(containers[i].querySelectorAll('textarea'));

      for (var l=0; l<textareas.length; ++l) {
      
        var t = textareas[l];
        if(t.value != "" || classes != 'inline-related has_original'){
          if (t.getAttribute('data-processed') == '0' && t.id.indexOf('__prefix__') == -1) {
            t.setAttribute('data-processed', '1');
            var ext = JSON.parse(t.getAttribute('data-external-plugin-resources'));
            for (var j=0; j<ext.length; ++j) {
              CKEDITOR.plugins.addExternal(ext[j][0], ext[j][1], ext[j][2]);
            }
            CKEDITOR.replace(t.id, JSON.parse(t.getAttribute('data-config')));
          }
       }
      }
    }
  }

  function initialiseCKEditorInInlinedForms() {
    document.body.addEventListener('click', function(e) {
      if (e.target && (
        e.target.matches('.add-row a') ||
        e.target.matches('.grp-add-handler')
      )) {
        initialiseCKEditor();
      }
    });
  }

}());
