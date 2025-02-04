import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { VikingService } from '../../../services/viking.service';
import { Viking } from '../../../interfaces/viking.interface';

@Component({
  standalone: false,
  selector: 'app-viking-edit',
  templateUrl: './viking-edit.component.html',
  styleUrls: ['./viking-edit.component.scss']
})
export class VikingEditComponent implements OnInit {
  editForm: FormGroup;
  vikingId: number;
  viking: Viking;
  formStatus: { type: string; message: string } | null = null;

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
      characterName: ['', Validators.required],
      description: ['', Validators.required],
      pictureUrl: ['', [Validators.required, Validators.pattern('https?://.+')]]
    });
  }

  loadViking(): void {
    this.vikingService.getVikingById(this.vikingId).subscribe((viking) => {
      this.viking = viking;
      this.editForm.patchValue(viking);
    });
  }

  onSubmit(): void {
    if (this.editForm.invalid) {
      return;
    }

    this.vikingService.updateViking(this.vikingId, this.editForm.value).subscribe(
      () => {
        this.formStatus = { type: 'success', message: 'Viking updated successfully!' };
        setTimeout(() => {
          this.router.navigate(['/vikings']);
        }, 2000);
      },
      (error) => {
        this.formStatus = { type: 'error', message: `Update failed: ${error.message}` };
      }
    );
  }
}
