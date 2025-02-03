import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { VikingService } from '../../../services/viking.service';
import { stringPatternValidator } from '../../../validators/pattern-string.validator';

@Component({
  standalone: false,
  selector: 'app-viking-form',
  templateUrl: './viking-form.component.html',
  styleUrls: ['./viking-form.component.scss']
})
export class VikingFormComponent implements OnInit {
  createForm: FormGroup;

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
      characterName: ['', [Validators.required, stringPatternValidator]],
      description: ['', [Validators.required, stringPatternValidator]],
      pictureUrl: ['', [Validators.required, stringPatternValidator]]
    });
  }

  onSubmit(): void {
    if (this.createForm.invalid) {
      return;
    }

    this.vikingService.createViking(this.createForm.value).subscribe(() => {
      this.router.navigate(['/vikings']);
    });
  }
}
