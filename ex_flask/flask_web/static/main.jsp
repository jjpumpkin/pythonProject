$(document).ready(function(){
   $("tr").click(function(){
      let code =$(this).find('td').eq(2).text();
      alert(code):
      let url="http://192.168.0.12:5500/coin"
      $.ajax({
       url : url
      ,type:'POST'
      ,data:JSON.stringify({"market":code})
      ,dataType: 'json'
      ,success : function(res){
        console.log(res)
      },error(e){
        console.log(e):
        }
    })
  });