/**
 * 
 */

/****************************************************************************************
 * 
 * 		G L O A B L  V A R I A B L E S
 * 
 ****************************************************************************************/
var map = null;
var infoWindow = null;
var bounds = null;

/*****************************************************************************************
 * 
 *      I N I T I A L I S A T I O N
 * 
 *****************************************************************************************/
	function initMap() {
		
		/** map options **/
		var styles = {
			hide:
				[
					{
						featureType: 'poi.business',
						stylers: [{visibility: 'off'}]
					},
				    {
						featureType: 'transit',
						elementType: 'labels.icon',
						stylers: [{visibility: 'off'}]
				    }
				]
		};
	
		/**   c r e a t e  m a p  **/
	  map = new google.maps.Map(document.getElementById('map'), {
	    center: {lat: 13.734170, lng: 100.587654},
	    zoom: 13,
	    mapTypeControl: false
	  });
	  
	  /**  needed for client location **/
	  infoWindow = new google.maps.InfoWindow({map: map});
	  
	  
	  map.setOptions({styles: styles['hide']});
	  
	  /** events handlers **/
	  google.maps.event.addListener(map, 'bounds_changed', function() {
			var latNE = map.getBounds().getNorthEast().lat();
			var lngNE = map.getBounds().getNorthEast().lng();
			var latSW = map.getBounds().getSouthWest().lat();
			var lngSW = map.getBounds().getSouthWest().lng();
			$.ajax({
			   type: "POST",
			   url: "/map/bounds",
			   dataType: "json",
			   traditional: true,
			   data: {
				   "latne": latNE,
				   "lngne": lngNE,
				   "latsw": latSW,
				   "lngsw": lngSW
			   },
			   success: function(data) {
					console.log(JSON.stringify(data));
					$.each(data , function (k,v) {
						console.log(v[0]);
						putMarker(v[0],v[1]);
                    })
			   }
			});
		});

	}
	

/*************************************************************************************
 * 
 *    	G E O L O C A T I O N
 * 
 *************************************************************************************/	
	/** Try HTML5 geolocation.  **/
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(function(position) {
        var pos = {
          lat: position.coords.latitude,
          lng: position.coords.longitude
        };

        infoWindow.setPosition(pos);
        infoWindow.setContent('Location found.');
        map.setCenter(pos);
        console.log(pos);
      }, function() {
        handleLocationError(true, infoWindow, map.getCenter());
      });
    } else {
      // Browser doesn't support Geolocation
      handleLocationError(false, infoWindow, map.getCenter());
    }
    

    function putMarker(lat,lng){
    	var marker = new google.maps.Marker({
          position: {lat: lat, lng: lng},
          map: map
        });

	}
  
