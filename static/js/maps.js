function initMap() {
    var dublin = {lat: 53.3498, lng: -6.2603};
    var map = new google.maps.Map(
        document.getElementById('map'), {zoom: 14, center: dublin});
    var marker = new google.maps.Marker({position: dublin, map: map});
}

