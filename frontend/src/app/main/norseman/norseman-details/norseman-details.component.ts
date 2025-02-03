import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { NorsemanService } from '../../../services/norseman.service';
import { Norseman } from '../../../interfaces/norseman.interface';

@Component({
  standalone: false,
  selector: 'app-norseman-details',
  templateUrl: './norseman-details.component.html',
  styleUrls: ['./norseman-details.component.scss']
})
export class NorsemanDetailsComponent implements OnInit {
  norseman: Norseman;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private norsemanService: NorsemanService
  ) {}

  ngOnInit(): void {
    this.getNorsemanDetails();
  }

  getNorsemanDetails(): void {
    const id = +this.route.snapshot.paramMap.get('id');
    this.norsemanService.getNorsemanById(id).subscribe((norseman) => {
      this.norseman = norseman;
    });
  }

  goBack(): void {
    this.router.navigate(['/norsemans']);
  }
}
