import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NorsemanComponent } from './norseman.component';

describe('NorsemanComponent', () => {
  let component: NorsemanComponent;
  let fixture: ComponentFixture<NorsemanComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [NorsemanComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(NorsemanComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
