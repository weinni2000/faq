const {Component, onMounted} = owl;
import {registry} from "@web/core/registry";

export class EntrypointComponent extends Component {
    static template = "minimal_owl.EntrypointComponent";

    setup() {
        onMounted(async () => {
            const popoverTriggerList = [].slice.call(
                document.querySelectorAll('[data-bs-toggle="popover"]')
            );
            popoverTriggerList.forEach(function (popoverTriggerEl) {
                /* eslint-disable no-undef */
                new bootstrap.Popover(popoverTriggerEl);
            });

            /* eslint-disable no-unused-vars */
            var popover = new bootstrap.Popover(
                document.querySelector(".popover-dismiss"),
                {
                    trigger: "focus",
                }
            );
        });
    }
}
registry
    .category("public_components")
    .add("minimal_owl.entrypoint_component", EntrypointComponent);
