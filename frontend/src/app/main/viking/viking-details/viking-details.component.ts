import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { VikingService } from '../../../services/viking.service';
import { FrontendViking } from '../../../models/viking.model'; 

@Component({
  standalone: false,
  selector: 'app-viking-details',
  templateUrl: './viking-details.component.html',
  styleUrls: ['./viking-details.component.scss']
})
export class VikingDetailsComponent implements OnInit {
  viking: FrontendViking;

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
    this.vikingService.getVikingById(id).subscribe((response) => {
      if (response && response.data) {
        this.viking = FrontendViking.fromBackend(response.data[0]); 
      }
    });
  }

  goBack(): void {
    this.router.navigate(['/vikings']);
  }
}
