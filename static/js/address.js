$(document).ready(function(){
    $("#id_province").change(function () {
      var url = $("#addressForm").attr("data-districts-url");  // get the url of the `load-districts` view
      var pId = $(this).val();  // get the selected province ID from the HTML input
      console.log('Hello world')
      $.ajax({                       // initialize an AJAX request
        url: url,                    // set the url of the request (= localhost:8000/dropdown/ajax/load-districts/)
        data: {
          'province': pId       // add the province id to the GET parameters
        },
        success: function (data) {   // `data` is the return of the `load_districts` view function
          $("#id_district").html(data);  // replace the contents of the district input with the data that came from the server
        }
      });

    });


    $("#id_district").change(function () {
      var url = $("#addressForm").attr("data-municipalities-url");  // get the url of the `load-municipalities` view
      var dId = $(this).val();  // get the selected district ID from the HTML input

      $.ajax({                       // initialize an AJAX request
        url: url,                    // set the url of the request (= localhost:8000/dropdown/ajax/load-municipalities/)
        data: {
          'district': dId       // add the district id to the GET parameters
        },
        success: function (data) {   // `data` is the return of the `load_municipalities` view function
          $("#id_municipality").html(data);  // replace the contents of the municipality input with the data that came from the server
        }
      });

    });

    $("#id_office_province").change(function () {
      var url = $("#addressForm").attr("data-office-districts-url");  // get the url of the `load-office-districts` view
      var opId = $(this).val();  // get the selected office province ID from the HTML input

      $.ajax({                       // initialize an AJAX request
        url: url,                    // set the url of the request (= localhost:8000/dropdown/ajax/load-office-districts/)
        data: {
          'office_province': opId       // add the office province id to the GET parameters
        },
        success: function (data) {   // `data` is the return of the `load_office_districts` view function
          $("#id_office_district").html(data);  // replace the contents of the office district input with the data that came from the server
        }
      });

    });


    $("#id_office_district").change(function () {
      var url = $("#addressForm").attr("data-office-municipalities-url");  // get the url of the `load-office-municipalities` view
      var odId = $(this).val();  // get the selected office district ID from the HTML input

      $.ajax({                       // initialize an AJAX request
        url: url,                    // set the url of the request (= localhost:8000/dropdown/ajax/load-office-municipalities/)
        data: {
          'office_district': odId       // add the office district id to the GET parameters
        },
        success: function (data) {   // `data` is the return of the `load_office_municipalities` view function
          $("#id_office_municipality").html(data);  // replace the contents of the office municipality input with the data that came from the server
        }
      });

    });


    $("#id_permanent_province").change(function () {
      var url = $("#addressForm").attr("data-permanent-districts-url");  // get the url of the `load-permanent-districts` view
      var ppId = $(this).val();  // get the selected permanent province ID from the HTML input

      $.ajax({                       // initialize an AJAX request
        url: url,                    // set the url of the request (= localhost:8000/dropdown/ajax/load-permanent-districts/)
        data: {
          'permanent_province': ppId       // add the permanent province id to the GET parameters
        },
        success: function (data) {   // `data` is the return of the `load_permanent_districts` view function
          $("#id_permanent_district").html(data);  // replace the contents of the permanent district input with the data that came from the server
        }
      });

    });

    $("#id_temporary_province").change(function () {
      var url = $("#addressForm").attr("data-temporary-districts-url");  // get the url of the `load-temporary-districts` view
      var tpId = $(this).val();  // get the selected temporary province ID from the HTML input

      $.ajax({                       // initialize an AJAX request
        url: url,                    // set the url of the request (= localhost:8000/dropdown/ajax/load-temporary-districts/)
        data: {
          'temporary_province': tpId       // add the temporary province id to the GET parameters
        },
        success: function (data) {   // `data` is the return of the `load_temporary_districts` view function
          $("#id_temporary_district").html(data);  // replace the contents of the temporary district input with the data that came from the server
        }
      });

    });


    $("#id_permanent_district").change(function () {
      var url = $("#addressForm").attr("data-permanent-municipalities-url");  // get the url of the `load-permanent-municipalities` view
      var pdId = $(this).val();  // get the selected permanent district ID from the HTML input

      $.ajax({                       // initialize an AJAX request
        url: url,                    // set the url of the request (= localhost:8000/dropdown/ajax/load-permanent-municipalities/)
        data: {
          'permanent_district': pdId       // add the permanent district id to the GET parameters
        },
        success: function (data) {   // `data` is the return of the `load_permanent_municipalities` view function
          $("#id_permanent_municipality").html(data);  // replace the contents of the permanent municipality input with the data that came from the server
        }
      });

    });

    $("#id_temporary_district").change(function () {
      var url = $("#addressForm").attr("data-temporary-municipalities-url");  // get the url of the `load-temporary-municipalities` view
      var tdId = $(this).val();  // get the selected temporary district ID from the HTML input

      $.ajax({                       // initialize an AJAX request
        url: url,                    // set the url of the request (= localhost:8000/dropdown/ajax/load-temporary-municipalities/)
        data: {
          'temporary_district': tdId       // add the temporary district id to the GET parameters
        },
        success: function (data) {   // `data` is the return of the `load_temporary_municipalities` view function
          $("#id_temporary_municipality").html(data);  // replace the contents of the temporary municipality input with the data that came from the server
        }
      });

    });
});
