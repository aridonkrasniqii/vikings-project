import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { NorsemanService } from '../../../services/norseman.service';


@Component({
  standalone: false,
  selector: 'app-norseman-edit',
  templateUrl: './norseman-edit.component.html',
  styleUrls: ['./norseman-edit.component.scss']
})
export class NorsemanEditComponent implements OnInit {
  editForm: FormGroup;
  norsemanId: number;

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
      pictureUrl: ['', Validators.required]
    });
  }

  loadNorseman(): void {
    this.norsemanService.getNorsemanById(this.norsemanId).subscribe((norseman) => {
      this.editForm.patchValue(norseman);
    });
  }

  onSubmit(): void {
    if (this.editForm.invalid) {
      return;
    }

    this.norsemanService.updateNorseman(this.norsemanId, this.editForm.value).subscribe(() => {
      this.router.navigate(['/norsemans']);
    });
  }
}
