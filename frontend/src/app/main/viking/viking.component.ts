import { Component } from '@angular/core';
import { VikingService } from '../../services/viking.service';


@Component({
  standalone: false,
  selector: 'app-viking',
  templateUrl: './viking.component.html',
  styleUrls: ['./viking.component.css']
})
export class VikingComponent {
  
  constructor(private vikingService: VikingService) {}

  ngOnInit(): void {
  
  }
}
 