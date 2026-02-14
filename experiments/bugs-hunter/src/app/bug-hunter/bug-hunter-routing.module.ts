import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { BugHunterPage } from './bug-hunter.page';

const routes: Routes = [
  {
    path: '',
    component: BugHunterPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class BugHunterPageRoutingModule {}
