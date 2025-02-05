import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NorsemanFormComponent } from './norseman-form.component';

describe('NorsemanFormComponent', () => {
  let component: NorsemanFormComponent;
  let fixture: ComponentFixture<NorsemanFormComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [NorsemanFormComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(NorsemanFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
