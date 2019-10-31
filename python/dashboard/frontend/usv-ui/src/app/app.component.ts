import { Component } from '@angular/core';

// export code for grid list
export interface Tile {
  color: string;
  cols: number;
  rows: number;
  text: string;
}

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'usv-ui';
  

  // TODO: Center on GPS coord on start rather than fixed location
  lat = 45.4122448;
  lng = -75.7107264;

  locationChosen = false;

  tiles: Tile[] = [
    {text: 'Camera feed goes here!', cols: 2, rows: 1, color: 'lightblue'},
    {text: 'Google Maps', cols: 1, rows: 1, color: 'lightgreen'},
  ];

  onChosenLocation(event) {
    console.log(event)
    this.lat = event.coords.lat;
    this.lng = event.coords.lng;
    this.locationChosen = true;
  }
}