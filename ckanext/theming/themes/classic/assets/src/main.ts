/// <reference path="../../../../../../types.d.ts" />

import { button } from "./util";
import { Modal } from "./modal";
import { Notification } from "./notification";
import { Tooltip } from "./tooltip";
import { Popover } from "./popover";

((ckan) => {
  const ui: IUi = {
    button: button,

    modal: Modal.create,
    getModal: Modal.byId,

    notification: Notification.create,
    getNotification: Notification.byId,

    tooltip: Tooltip.create,
    getTooltip: Tooltip.byId,

    popover: Popover.create,
    getPopover: Popover.byId,
  };

  ckan.sandbox.setup((sb) => {
    sb.ui = sb.ui || {};
    Object.assign(sb.ui, ui);
  });
})(window.ckan);
