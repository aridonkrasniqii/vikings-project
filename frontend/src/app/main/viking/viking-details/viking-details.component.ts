import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { VikingService } from '../../../services/viking.service';
import { Viking } from '../../../interfaces/viking.interface';

@Component({
  standalone: false,
  selector: 'app-viking-details',
  templateUrl: './viking-details.component.html',
  styleUrls: ['./viking-details.component.scss']
})
export class VikingDetailsComponent implements OnInit {
  viking: Viking;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private vikingService: VikingService
  ) {}

  ngOnInit(): void {
    this.getVikingDetails();
  }

  getVikingDetails(): void {
    const id = +this.route.snapshot.paramMap.get('id');
    this.vikingService.getVikingById(id).subscribe((viking) => {
      this.viking = viking;
    });
  }

  goBack(): void {
    this.router.navigate(['/vikings']);
  }
}
