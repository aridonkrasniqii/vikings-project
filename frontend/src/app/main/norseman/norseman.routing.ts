import { NgModule } from '@angular/core';
import { Route, RouterModule } from '@angular/router';
import { NorsemanComponent } from './norseman.component';
import { NorsemanEditComponent } from './norseman-edit/norseman-edit.component';
import { NorsemanDetailsComponent } from './norseman-details/norseman-details.component';
import { NorsemanTableComponent } from './norseman-table/norseman-table.component';

const norsemanRoutes: Route[] = [
  {
    path: '',
    component: NorsemanComponent,
    children: [
      {
        path: '',
        component: NorsemanTableComponent
      },
      {
        path: 'edit/:id',
        component: NorsemanEditComponent
      },
      {
        path: 'details/:id',
        component: NorsemanDetailsComponent
      }
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(norsemanRoutes)],
  exports: [RouterModule]
})
export class NorsemanRoutingModule{ }
