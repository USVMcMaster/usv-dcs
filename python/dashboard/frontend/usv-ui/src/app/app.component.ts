import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'usv-ui';
  
  // TODO: Center on GPS coord on start rather than fixed location
  init_lat = 43.266951;
  init_lng = -79.921734;
  init_zoom = 15;

  marker_lat;
  marker_lng;
  map_url;

  locationChosen = false;

  onChosenLocation(event) {
    console.log(event)
    this.marker_lat = event.coords.lat;
    this.marker_lng = event.coords.lng;
    this.locationChosen = true;
  }

  gen_map_snapshot() {
    var static_map_url = "https://maps.googleapis.com/maps/api/staticmap?";

    // Map Center
    static_map_url += "center=" + this.init_lat + "," + this.init_lng;

    // Map Zoom Level
    static_map_url += "&zoom=" + this.init_zoom;

    // Map Size
    static_map_url += "&size=" + "480x480";

    // Map Marker
    static_map_url += "&markers=" + this.marker_lat + "," + this.marker_lng;

    // Remove all text
    static_map_url += "&style=" + "feature:all|element:labels|visibility:off";

    // Remove Roads
    static_map_url += "&style=" + "feature:road|visibility:off";

    // Appending Key
    static_map_url += "&key=" + 'AIzaSyDdjnJdmnyoNX2btE-w8MHDdeTPhQgb6cs';

    return static_map_url;

  }

  gen_path_handler(event) {
    console.log(this.init_lat, this.init_lng, this.init_zoom, event)
    console.log(this.gen_map_snapshot())
    this.map_url = this.gen_map_snapshot()
  }
}