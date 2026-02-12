import { NgModule } from '@angular/core';
import { PreloadAllModules, RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
    path: 'bug-hunter',
    loadChildren: () => import('./bug-hunter/bug-hunter.module').then( m => m.BugHunterPageModule)
  },
  {
    path: '**',
    redirectTo: 'bug-hunter',
    pathMatch: 'full'
  },
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules })
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
