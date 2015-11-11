function menu() {
  var estadoMenu = document.getElementById('navbar');
  if(estadoMenu.className=='visible'){
    estadoMenu.className='oculto';
  }else{
    estadoMenu.className='visible';
  }
}
