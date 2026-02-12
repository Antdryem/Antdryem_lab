import { Component, OnInit } from '@angular/core';
interface bugs {
  img: string,
  x: number,
  y: number,
  alt: string,
  rotation: number,
}
@Component({
  selector: 'app-bug-hunter',
  templateUrl: './bug-hunter.page.html',
  styleUrls: ['./bug-hunter.page.scss'],
})
export class BugHunterPage implements OnInit {
  seconds: number = 0;
  score: number = 0;
  bugs: bugs[] = [];
  constructor() {

    this.insectIsBorn();

  }

  ngOnInit() {
  }

  insectIsBorn() {
    const width = window.innerWidth
    const height = window.innerHeight

    var insectN: number = Math.ceil(Math.random() * 4);


    this.bugs.push({
      img: (insectN === 4 ? "http://pngimg.com/uploads/fly/fly_PNG3946.png" : insectN === 3 ?
        "http://pngimg.com/uploads/mosquito/mosquito_PNG18175.png" : insectN === 2 ?
          "http://pngimg.com/uploads/spider/spider_PNG12.png" : insectN === 1 ?
            "http://pngimg.com/uploads/roach/roach_PNG12163.png" :
            "http://pngimg.com/uploads/roach/roach_PNG12163.png"),
      x: this.getRandomRange(-width * .4, height * .4),//: Math.random() * (width - 200) + 50,
      y: this.getRandomRange(-height * .4, height * .4),//Math.random() * (height - 100) + 50,
      alt: (insectN === 4 ? "Fly" : insectN === 3 ?
        "Mosquito" : insectN === 2 ?
          "Spider" : insectN === 1 ?
            "Roach" :
            "Roach"),
      rotation: Math.ceil(Math.random() * 360)
    });
  }

  getRandomRange(min: number, max: number) {
    return Math.random() * (max - min) + min;
  }
  deleteBug(n:number) {
    this.deleteId(n);
    //this.bugs = this.bugs.slice(n, n+1);
    setTimeout( () => {
    this.insectIsBorn();
      setTimeout(()=>{
        this.insectIsBorn();
      }, Math.random() * 3000)
    }, 1000);
  }

  deleteId(n:number) {
    var out: bugs[] = [];
    console.log(n, this.bugs );
    
    this.bugs.forEach((bug, i)=>{
        console.log(n,i, n!==i);
      
      if(!(n==i)) {
        
        out.push(bug);
      }
    });
    console.log("esteeeeeeeee", out);
    
    this.bugs = out;
  }

}
