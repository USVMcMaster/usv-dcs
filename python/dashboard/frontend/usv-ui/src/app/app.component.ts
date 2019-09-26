import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'usv-ui';
  
  lat = 45.4122448;
  lng = -75.7107264;

  locationChosen = false;

  onChosenLocation(event) {
  	// console.log(event)
  	this.lat = event.coords.lat;
  	this.lng = event.coords.lng;
  	this.locationChosen = true;
  }
}