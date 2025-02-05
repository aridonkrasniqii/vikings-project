import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { NorsemanService } from '../../../services/norseman.service';
import { FrontendNorseman } from '../../../models/norseman.model';


@Component({
  standalone: false,
  selector: 'app-norseman-details',
  templateUrl: './norseman-details.component.html',
  styleUrls: ['./norseman-details.component.scss']
})
export class NorsemanDetailsComponent implements OnInit {
  norseman: FrontendNorseman;

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
    this.norsemanService.getNorsemanById(id).subscribe((response) => {
      this.norseman = FrontendNorseman.fromBackend(response.data);
    });
  }

  goBack(): void {
    this.router.navigate(['/norsemans']);
  }
}
