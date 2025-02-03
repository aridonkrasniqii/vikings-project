import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { VikingTableComponent } from './viking/viking-table/viking-table.component';
import { NflPlayerTableComponent } from './nfl-player/nflplayer-table/nflplayer-table.component';
import { NorsemanTableComponent } from './norseman/norseman-table/norseman-table.component';
import { VikingDetailsComponent } from './viking/viking-details/viking-details.component';
import { NflPlayerDetailsComponent } from './nfl-player/nflplayer-details/nflplayer-details.component';
import { NorsemanDetailsComponent } from './norseman/norseman-details/norseman-details.component';
import { VikingEditComponent } from './viking/viking-edit/viking-edit.component';
import { NflPlayerEditComponent } from './nfl-player/nflplayer-edit/nflplayer-edit.component';
import { NorsemanEditComponent } from './norseman/norseman-edit/norseman-edit.component';
import { MainComponent } from './main.component';
import { VikingFormComponent } from './viking/viking-form/viking-form.component';

const routes: Routes = [{
  path: '',
  component: MainComponent,
  children: [
    // Routes for Viking domain
    {
      path: 'vikings',
      component: VikingTableComponent
    },
    {
      path: 'vikings/details/:id',
      component: VikingDetailsComponent
    },
    {
      path: 'vikings/form',
      component: VikingFormComponent
    },
    {
      path: 'vikings/edit/:id',
      component: VikingEditComponent
    },

    // Routes for NFL Player domain
    {
      path: 'nflplayers',
      component: NflPlayerTableComponent
    },
    {
      path: 'nflplayers/details/:id',
      component: NflPlayerDetailsComponent
    },
    {
      path: 'nflplayers/edit/:id',
      component: NflPlayerEditComponent
    },

    // Routes for Norseman domain
    {
      path: 'norsemans',
      component: NorsemanTableComponent
    },
    {
      path: 'norsemans/details/:id',
      component: NorsemanDetailsComponent
    },
    {
      path: 'norsemans/edit/:id',
      component: NorsemanEditComponent
    },

    { path: '', redirectTo: '/vikings', pathMatch: 'full' },
    { path: '**', redirectTo: '/vikings' }  // Wildcard route for 404
  ]
}
];

@NgModule({
  imports: [
    RouterModule.forChild(routes)
  ],
  exports: [RouterModule]
})
export class MainRoutingModule { }
