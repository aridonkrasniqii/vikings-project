import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { VikingService } from '../../../services/viking.service';
import { FrontendViking } from '../../../models/viking.model'; 

@Component({
  standalone: false,
  selector: 'app-viking-edit',
  templateUrl: './viking-edit.component.html',
  styleUrls: ['./viking-edit.component.css']
})
export class VikingEditComponent implements OnInit {
  editForm: FormGroup;
  vikingId: number;
  viking: FrontendViking;
  formStatus: { type: string; message: string } | null = null;
  loading: boolean = true;

  constructor(
    private fb: FormBuilder,
    private route: ActivatedRoute,
    private router: Router,
    private vikingService: VikingService
  ) {}

  ngOnInit(): void {
    this.vikingId = +this.route.snapshot.paramMap.get('id');
    this.createForm();
    this.loadViking();
  }

  createForm(): void {
    this.editForm = this.fb.group({
      name: ['', Validators.required],
      actorName: ['', Validators.required],
      description: ['', Validators.required],
      photo: ['', Validators.required ] // Validators.pattern('https?://.+')]
    });
  }

  loadViking(): void {
    this.vikingService.getVikingById(this.vikingId).subscribe({
      next: (response) => {
        if (response && response.data) {
          this.viking = FrontendViking.fromBackend(response.data[0]);
          this.editForm.patchValue(this.viking);
        }
        this.loading = false;
      },
      error: (error) => {
        console.error('Error loading Viking:', error);
        this.formStatus = { type: 'error', message: `Failed to load Viking: ${error.message}` };
        this.loading = false;
      }
    });
  }

  onSubmit(): void {
    if (this.editForm.invalid) {
      return;
    }

    this.updateViking();
  }

  private updateViking() { 
    const updatedViking = new FrontendViking({
      name: this.editForm.value.name,
      actorName: this.editForm.value.actorName,
      description: this.editForm.value.description,
      photo: this.editForm.value.pictureUrl
    });

    this.vikingService.updateViking(this.vikingId, updatedViking).subscribe({
      next: () => {
        this.formStatus = { type: 'success', message: 'Viking updated successfully!' };
        setTimeout(() => {
          this.router.navigate(['/vikings']);
        }, 2000);
      },
      error: (error) => {
        this.formStatus = { type: 'error', message: `Update failed: ${error.message}` };
      }
    });
  }
}
