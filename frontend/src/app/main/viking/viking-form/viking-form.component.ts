import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { VikingService } from '../../../services/viking.service';
import { FrontendViking, BackendViking } from '../../../models/viking.model'; // Import models
import { stringPatternValidator } from '../../../validators/pattern-string.validator';

@Component({
  standalone: false,
  selector: 'app-viking-form',
  templateUrl: './viking-form.component.html',
  styleUrls: ['./viking-form.component.css']
})
export class VikingFormComponent implements OnInit {
  createForm: FormGroup;
  successMessage: string = '';
  errorMessage: string = '';

  constructor(
    private fb: FormBuilder,
    private router: Router,
    private vikingService: VikingService
  ) { }

  ngOnInit(): void {
    this.initForm();
  }

  initForm(): void {
    this.createForm = this.fb.group({
      name: ['', [Validators.required, stringPatternValidator]],
      actorName: ['', [Validators.required, stringPatternValidator]],
      description: ['', [Validators.required]],
      pictureUrl: ['', Validators.required]
    });
  }

  onSubmit(): void {
    if (this.createForm.invalid) {
      return;
    }

    this.createViking()
  }

  private createViking() {
    const frontendViking = new FrontendViking({
      name: this.createForm.value.name,
      actorName: this.createForm.value.actorName,
      description: this.createForm.value.description,
      photo: this.createForm.value.pictureUrl
    });
    this.vikingService.createViking(frontendViking).subscribe({
      next: () => {
        this.successMessage = 'Viking created successfully!';
        setTimeout(() => {
          this.successMessage = '';
          this.router.navigate(['/vikings']);
        }, 2000);
      },
      error: (error) => {
        this.errorMessage = error.error?.message || 'An error occurred. Please try again.';
      }
    });
  }
}
