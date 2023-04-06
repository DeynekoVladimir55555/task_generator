$(document).ready(function() {
    $('#dark_theme').on('click', function () {
        $('.bg-light').addClass('bg-dark').removeClass('bg-light');
        $('.text-dark').addClass('text-light').removeClass('text-dark');

        $('#dark_theme').find('a').addClass('active');
        $('#light_theme').find('a').removeClass('active');
    });

    $('#light_theme').on('click', function () {
        $('.bg-dark').addClass('bg-light').removeClass('bg-dark');
        $('.text-light').addClass('text-dark').removeClass('text-light');

        $('#dark_theme').find('a').removeClass('active');
        $('#light_theme').find('a').addClass('active');
    });

    $(".dynamic_blocking").attr("disabled", true);

    $('#blocking_item').change(function() {
      if (this.checked) {
        $(".dynamic_blocking").removeAttr("disabled");
      } else {
        $(".dynamic_blocking").attr("disabled", true);
      }
    });
});