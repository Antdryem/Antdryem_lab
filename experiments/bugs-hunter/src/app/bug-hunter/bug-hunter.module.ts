import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { BugHunterPageRoutingModule } from './bug-hunter-routing.module';

import { BugHunterPage } from './bug-hunter.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    BugHunterPageRoutingModule
  ],
  declarations: [BugHunterPage]
})
export class BugHunterPageModule {}
