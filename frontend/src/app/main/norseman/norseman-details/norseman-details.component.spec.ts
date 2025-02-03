import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NorsemanDetailsComponent } from './norseman-details.component';

describe('NorsemanDetailsComponent', () => {
  let component: NorsemanDetailsComponent;
  let fixture: ComponentFixture<NorsemanDetailsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [NorsemanDetailsComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(NorsemanDetailsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
