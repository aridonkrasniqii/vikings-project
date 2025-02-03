import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NorsemanEditComponent } from './norseman-edit.component';

describe('NorsemanEditComponent', () => {
  let component: NorsemanEditComponent;
  let fixture: ComponentFixture<NorsemanEditComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [NorsemanEditComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(NorsemanEditComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
