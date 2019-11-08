import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AgmCoreModule } from '@agm/core';
import { AppComponent } from './app.component';
import { NgOpenCVModule, OpenCVOptions } from 'ng-open-cv';
import { MatCardModule, MatGridListModule, MatButtonModule } from '@angular/material';

const openCVConfig: OpenCVOptions = {
  scriptUrl: 'assets/opencv/asm/3.4/opencv.js'
};

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    AgmCoreModule.forRoot({
      apiKey: 'AIzaSyDdjnJdmnyoNX2btE-w8MHDdeTPhQgb6cs'
    }),
    NgOpenCVModule.forRoot(openCVConfig),
    MatCardModule,
    MatGridListModule,
    MatButtonModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
