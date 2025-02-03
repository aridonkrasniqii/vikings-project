import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NorsemanTableComponent } from './norseman-table.component';

describe('NorsemanTableComponent', () => {
  let component: NorsemanTableComponent;
  let fixture: ComponentFixture<NorsemanTableComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [NorsemanTableComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(NorsemanTableComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
