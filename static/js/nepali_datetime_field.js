$(document).ready(function(){
    $('.nepalidateinput').nepaliDatePicker({
        dateFormat: '%D, %M %d, %y',
        closeOnDateSelect: true,
        minDate: 'सोम, जेठ १०, २०७३',
        maxDate: 'मंगल, जेठ ३२, २०७३'
});
});