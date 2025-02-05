import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { NorsemanService } from '../../../services/norseman.service';
import { FrontendNorseman } from '../../../models/norseman.model'; // Import FrontendNorseman model

@Component({
  standalone: false,
  selector: 'app-norseman-edit',
  templateUrl: './norseman-edit.component.html',
  styleUrls: ['./norseman-edit.component.css']
})
export class NorsemanEditComponent implements OnInit {
  editForm: FormGroup;
  norsemanId: number;
  norseman: FrontendNorseman;
  formStatus: { type: string; message: string } | null = null;
  loading: boolean = true;

  constructor(
    private fb: FormBuilder,
    private route: ActivatedRoute,
    private router: Router,
    private norsemanService: NorsemanService
  ) {}

  ngOnInit(): void {
    this.norsemanId = +this.route.snapshot.paramMap.get('id');
    this.createForm();
    this.loadNorseman();
  }

  createForm(): void {
    this.editForm = this.fb.group({
      name: ['', Validators.required],
      actorName: ['', Validators.required],
      characterName: ['', Validators.required],
      description: ['', Validators.required],
      photo: ['', Validators.required] // Updated field name to 'photo'
    });
  }

  loadNorseman(): void {
    this.norsemanService.getNorsemanById(this.norsemanId).subscribe({
      next: (response) => {
        if (response && response.data) {
          this.norseman = FrontendNorseman.fromBackend(response.data[0]); // Convert BackendNorseman to FrontendNorseman
          this.editForm.patchValue(this.norseman);
        }
        this.loading = false;
      },
      error: (error) => {
        console.error('Error loading Norseman:', error);
        this.formStatus = { type: 'error', message: `Failed to load Norseman: ${error.message}` };
        this.loading = false;
      }
    });
  }

  onSubmit(): void {
    if (this.editForm.invalid) {
      return;
    }

    this.updateNorseman();
  }

  private updateNorseman() {
    const updatedNorseman = new FrontendNorseman({
      name: this.editForm.value.name,
      actorName: this.editForm.value.actorName,
      description: this.editForm.value.description,
      photo: this.editForm.value.photo // Updated field name to 'photo'
    });

    this.norsemanService.updateNorseman(this.norsemanId, updatedNorseman).subscribe({
      next: () => {
        this.formStatus = { type: 'success', message: 'Norseman updated successfully!' };
        setTimeout(() => {
          this.router.navigate(['/norsemans']);
        }, 2000);
      },
      error: (error) => {
        this.formStatus = { type: 'error', message: `Update failed: ${error.message}` };
      }
    });
  }
}
