import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { VikingService } from '../../../services/viking.service';


@Component({
  standalone: false,
  selector: 'app-viking-edit',
  templateUrl: './viking-edit.component.html',
  styleUrls: ['./viking-edit.component.scss']
})
export class VikingEditComponent implements OnInit {
  editForm: FormGroup;
  vikingId: number;

  constructor(
    private fb: FormBuilder,
    private route: ActivatedRoute,
    private router: Router,
    private vikingService: VikingService
  ) {}

  ngOnInit(): void {
    this.vikingId = +this.route.snapshot.paramMap.get('id');
    this.initForm();
    this.loadViking();
  }

  initForm(): void {
    this.editForm = this.fb.group({
      name: ['', Validators.required],
      actorName: ['', Validators.required],
      characterName: ['', Validators.required],
      description: ['', Validators.required],
      pictureUrl: ['', Validators.required]
    });
  }

  loadViking(): void {
    this.vikingService.getVikingById(this.vikingId).subscribe((viking) => {
      this.editForm.patchValue(viking);
    });
  }

  onSubmit(): void {
    if (this.editForm.invalid) {
      return;
    }

    this.vikingService.updateViking(this.vikingId, this.editForm.value).subscribe(() => {
      this.router.navigate(['/vikings']);
    });
  }
}
