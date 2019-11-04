(function($) {

$containers =    $('.has_original');
$inputs = $containers.find('input:text').filter(function() {
     return this.value == ""; })

     $inputs.parent().hide();

$inputs = $containers.find('textarea').filter(function() {
        return this.value == ""; })
        
        $inputs.parent().parent().parent().hide()


          $('div.inline-group').draggable({
              items: 'tr.has_original',
              handle: 'td',
              update: function() {
                  $(this).find('tr.has_original').each(function(i) {
                      $(this).find('input[name$=order]').val(i+1);
                      $(this).removeClass('row1').removeClass('row2');
                      $(this).addClass('row'+((i%2)+1));
                  });
              }
          });
          $('tr.has_original').css('cursor', 'move');
   


})(django.jQuery);



/*function initialiseCKEditor() {
    var containers = document.getElementsByClassName('inline-related ');
    console.log( containers);
    for (var i=0; i<containers.length; ++i) {
    var classes = containers[i].className;
    console.log(classes);
    var textareas = Array.prototype.slice.call(containers[i].querySelectorAll('textarea'));
    console.log( textareas);
      for (var l=0; l<textareas.length; ++l) {
        console.log( textareas);
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
  } */