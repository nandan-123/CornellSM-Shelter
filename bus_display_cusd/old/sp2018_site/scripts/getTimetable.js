function getTimetable() {
  var token = 'Bearer e5159b89-86c1-3cca-8412-59de037c674b';
  return $.ajax({
    url: 'https://gateway.api.cloud.wso2.com:443/t/mystop/tcat/v1/rest/StopDepartures/Get/165',
    type: 'GET',
    dataType: 'json',
    beforeSend: function(xhr) {
      xhr.setRequestHeader("Authorization", token);
    },
    //data: 'json=' + escape(JSON.stringify(createRequestObject)),
    success: function(msg) {
      var data = JSON.stringify(msg);
      //TimeTable(msg);
    },
    error: function(XMLHttpRequest, textStatus, errorThrown) {
      alert(errorThrown);
    }
  });
}