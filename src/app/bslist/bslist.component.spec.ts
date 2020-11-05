import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BslistComponent } from './bslist.component';

describe('BslistComponent', () => {
  let component: BslistComponent;
  let fixture: ComponentFixture<BslistComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ BslistComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(BslistComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
