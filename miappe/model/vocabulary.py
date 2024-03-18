from typing import TYPE_CHECKING, Optional

from litestar.dto import dto_field
from sqlalchemy.orm import Mapped, mapped_column, relationship

from miappe.model.base import Base

if TYPE_CHECKING:
    from miappe.model.device import Device
    from miappe.model.method import Method
    from miappe.model.unit import Unit
    from miappe.model.variable import Variable
    from miappe.model.event import Event


class Vocabulary(Base):
    __tablename__: str = "vocabulary_table"  # type: ignore

    external_reference: Mapped[Optional[str]]

    # Todo: Make namespace a separate entity?
    namespace: Mapped[Optional[str]] = mapped_column(server_default="APPN")

    # Todo: use the same terminologies as PHIS - extract, widening, narrowing?
    relationship_type: Mapped[Optional[str]]

    # Relationships
    device: Mapped[list["Device"]] = relationship(
        back_populates="device_type", lazy="selectin", info=dto_field("private")
    )
    method: Mapped[list["Method"]] = relationship(
        back_populates="method_type", lazy="selectin", info=dto_field("private")
    )
    unit: Mapped[list["Unit"]] = relationship(
        back_populates="unit_type", lazy="selectin", info=dto_field("private")
    )
    variable: Mapped[list["Variable"]] = relationship(
        back_populates="variable_type", lazy="selectin", info=dto_field("private")
    )
    event: Mapped[list["Event"]] = relationship(
        back_populates="event_type", lazy="selectin", info=dto_field("private")
    )
