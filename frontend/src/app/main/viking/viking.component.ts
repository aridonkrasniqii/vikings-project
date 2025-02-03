import { Component } from '@angular/core';
import { Viking } from '../../interfaces/viking.interface';
import { VikingService } from '../../services/viking.service';


@Component({
  standalone: false,
  selector: 'app-viking',
  templateUrl: './viking.component.html',
  styleUrls: ['./viking.component.css']
})
export class VikingComponent {
  vikings: Viking[] = [];
  viking: Viking;

  constructor(private vikingService: VikingService) {}

  ngOnInit(): void {
    // this.getVikings();
  }

  getVikings() {
    this.vikingService.getAllVikings().subscribe((vikings: Viking[]) => {
      this.vikings = vikings;
    });
  }

  getVikingById(id: number) {
    this.vikingService.getVikingById(id).subscribe((viking: Viking) => {
      this.viking = viking;
    });
  }

  updateViking(id: number, data: Partial<Viking>) {
    this.vikingService
      .updateViking(id, data)
      .subscribe((updatedViking: Viking) => {
        this.vikings = this.vikings.map(viking =>
          viking.id === id ? updatedViking : viking
        );
      });
  }

  deleteViking(id: number) {
    this.vikingService
      .deleteViking(id)
      .subscribe((deletedViking: Viking) => {
        this.vikings = this.vikings.filter(
          viking => viking.id !== deletedViking.id
        );
      });
  }
}
 