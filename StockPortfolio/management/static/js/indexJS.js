console.log("indexJS2");

function json2table(jsonf) {
  let cuerpoTabla = $("#cuerpoTabla");
  let count = 0;

  for (i in jsonf) {
    tr = $('<tr/>');
    count++;
    if (count > 6) {
      tr.append("<td>" + i + "</td>");
      tr.append("<td>" + jsonf[i]["1. open"] + "</td>");
      tr.append("<td>" + jsonf[i]["2. high"] + "</td>");
      tr.append("<td>" + jsonf[i]["3. low"] + "</td>");
      tr.append("<td>" + jsonf[i]["4. close"] + "</td>");
      tr.append("<td>" + jsonf[i]["5. volume"] + "</td>");
    }
    cuerpoTabla.append(tr);
  }
  //attached more info
  $("#info").val(jsonf["1. Information"]);
  $("#symbol").val(jsonf["2. Symbol"]);
  $("#refreshed").val(jsonf["3. Last Refreshed"]);
  $("#interval").val(jsonf["4. Interval"]);
  $("#size").val(jsonf["5. Output Size"]);
  $("#time").val(jsonf["6. Time Zone"]);
  $("#price").val(jsonf[jsonf["3. Last Refreshed"]]["4. close"]);
}

$(document).ready(function() {
  //$('#myTable').DataTable();
});




/*
let count = Object.keys(jsonf).length

  tr.append("<td>" + jsonf["1. Information"] + "</td>");
  tr.append("<td>" + jsonf["2. Symbol"] + "</td>");
  tr.append("<td>" + jsonf["3. Last Refreshed"] + "</td>");
  tr.append("<td>" + jsonf["4. Interval"] + "</td>");
  tr.append("<td>" + jsonf["5. Output Size"] + "</td>");
  tr.append("<td>" + jsonf["6. Time Zone"] + "</td>");

  tr.append("<td>" + jsonf[jsonf["3. Last Refreshed"]]['1. open'] + "</td>");
  tr.append("<td>" + jsonf[jsonf["3. Last Refreshed"]]['2. high'] + "</td>");
  tr.append("<td>" + jsonf[jsonf["3. Last Refreshed"]]['3. low'] + "</td>");
  tr.append("<td>" + jsonf[jsonf["3. Last Refreshed"]]['4. close'] + "</td>");
  tr.append("<td>" + jsonf[jsonf["3. Last Refreshed"]]['5. volume'] + "</td>");

  cuerpoTabla.append(tr);


  var arr = [ {"id":"10", "class": "child-of-9"}, {"id":"11", "classd": "child-of-10"}];

  for (var i = 0; i < arr.length; i++){
      var obj = arr[i];
      for (var key in obj){
          var attrName = key;
          var attrValue = obj[key];
  		console.log(attrName);
  		console.log(attrValue);
      }
  }
  for (i in jsonf) {
    tr = $('<tr/>');
    tr.append("<td>" + i + "</td>");
    tr.append("<td>" + jsonf[i] + "</td>");
    tr.append("<td>" + jsonf[i] + "</td>");
    tr.append("<td>" + jsonf[i] + "</td>");
    tr.append("<td>" + jsonf[i] + "</td>");
    tr.append("<td>" + jsonf[i] + "</td>");
    tr.append("<td>" + jsonf[i] + "</td>");

    cuerpoTabla.append(tr);
  }*/
