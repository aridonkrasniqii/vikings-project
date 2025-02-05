import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { NorsemanService } from '../../../services/norseman.service';
import { FrontendNorseman } from '../../../models/norseman.model';

@Component({
  standalone: false,
  selector: 'app-norseman-form',
  templateUrl: './norseman-form.component.html',
  styleUrls: ['./norseman-form.component.css']
})
export class NorsemanFormComponent implements OnInit {
  createForm: FormGroup;
  formStatus: { type: string; message: string } | null = null;

  constructor(
    private fb: FormBuilder,
    private router: Router,
    private norsemanService: NorsemanService
  ) {}

  ngOnInit(): void {
    this.initForm();
  }

  initForm(): void {
    this.createForm = this.fb.group({
      name: ['', Validators.required],
      actorName: ['', Validators.required],
      description: ['', Validators.required],
      photo: ['', Validators.required]
    });
  }

  onSubmit(): void {
    if (this.createForm.invalid) {
      return;
    }

    const newNorseman = new FrontendNorseman({
      name: this.createForm.value.name,
      actorName: this.createForm.value.actorName,
      description: this.createForm.value.description,
      photo: this.createForm.value.photo
    });

    this.norsemanService.createNorseman(newNorseman).subscribe({
      next: () => {
        this.formStatus = { type: 'success', message: 'Norseman created successfully!' };
        setTimeout(() => {
          this.formStatus = null;
          this.router.navigate(['/norsemans']);
        }, 2000);
      },
      error: (error) => {
        this.formStatus = { type: 'error', message: `Creation failed: ${error.message}` };
      }
    });
  }
}
