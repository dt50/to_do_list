 $(function() {
     $('input[name="daterange"]').daterangepicker({
             opens: 'left'
         },
         function(start, end, label) {
            window.location = "/task/filter/" + start.format('YYYY-MM-DD') + "/" + end.format('YYYY-MM-DD');
        }
     );
 });
