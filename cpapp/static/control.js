var database;
var initialize = function(){
};


function direkt(){
  var form=$('form1');
  $('dir').remove();
  $('indir').remove();
  form.insert('<input type="Text" id="Raumnr" name="Raumnr" label="Raumnr"/>');
  $('Raumnr').insert({before : '<div>', after: '</div>'});
  form.insert('<input type="Button" id="Weiter" name="Weiter" label="Weiter"  value="Weiter" onClick="validiereRaumnr();"/>');
  $('Weiter').insert({before : '<div>', after: '</div>'});
};

function validiereRaumnr(){
  var form=$('form1');
  var input=form['Raumnr']
  pattern=/^[A-Z][1-4]|E[0-9]{2}/;
  if(pattern.test($F(input).toUpperCase())){
    sucheraumnr();
  }
  else{
    console.log($('warnung1'));
    if($('warnung1')==null) 
      $('Raumnr').insert({after:'<p class="warnung" id="warnung1"> Eingabe muss aus Gebaeudebuchstaben gefolgt von Raumnr sein.</p>'});
  }

};

function indirekt(){
  var form=$('form1');
  $('dir').hide();
  $('indir').hide();
}

