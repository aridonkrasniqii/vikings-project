import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { VikingComponent } from './viking/viking.component';
import { NorsemanComponent } from './norseman/norseman.component';
import { NFLPlayerComponent } from './nfl-player/nfl-player.component';
import { VikingTableComponent } from './viking/viking-table/viking-table.component';
import { VikingDetailsComponent } from './viking/viking-details/viking-details.component';
import { VikingEditComponent } from './viking/viking-edit/viking-edit.component';
import { NorsemanDetailsComponent } from './norseman/norseman-details/norseman-details.component';
import { NorsemanEditComponent } from './norseman/norseman-edit/norseman-edit.component';
import { NorsemanTableComponent } from './norseman/norseman-table/norseman-table.component';


import { NFLPlayerEditComponent } from './nfl-player/nflplayer-edit/nflplayer-edit.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MainRoutingModule } from './main-routing.module';
import { MatPaginatorModule } from '@angular/material/paginator';
import { MatInputModule } from '@angular/material/input';
import { MatTableModule } from '@angular/material/table';
import { MainComponent } from './main.component';
import { RouterModule } from '@angular/router';
import { VikingService } from '../services/viking.service';
import { NorsemanService } from '../services/norseman.service';

import { HttpClient, HttpClientModule } from '@angular/common/http';
import { VikingFormComponent } from './viking/viking-form/viking-form.component';
import { NFLPlayerTableComponent } from './nfl-player/nflplayer-table/nflplayer-table.component';
import { NFLPlayerService } from '../services/nfl-player.service';
import { NFLPlayerDetailsComponent } from './nfl-player/nflplayer-details/nflplayer-details.component';
import { NFLPlayerFormComponent } from './nfl-player/nflplayer-form/nflplayer-form.component';
import { NorsemanFormComponent } from './norseman/norseman-form/norseman-form.component';


@NgModule({
  declarations: [
    VikingComponent,
    VikingTableComponent,
    VikingDetailsComponent,
    VikingEditComponent,
    VikingFormComponent,
    NorsemanComponent,
    NorsemanDetailsComponent,
    NorsemanEditComponent,
    NorsemanTableComponent,
    NorsemanFormComponent,
    NFLPlayerComponent,
    NFLPlayerDetailsComponent,
    NFLPlayerTableComponent,
    NFLPlayerEditComponent, 
    NFLPlayerFormComponent,
    MainComponent
],
  imports: [
    CommonModule,
    RouterModule,
    FormsModule,
    ReactiveFormsModule,
    MainRoutingModule,
    MatPaginatorModule,
    MatTableModule,
    MatInputModule,
    HttpClientModule
  ],
  providers: [VikingService, NorsemanService, NFLPlayerService]
})
export class MainModule { }
