<!DOCTYPE html>
<!-- saved from url=(0143)https://github.com/aws/amazon-sagemaker-examples/blob/master/sagemaker-python-sdk/scikit_learn_inference_pipeline/sklearn_abalone_featurizer.py -->
<html lang="en" data-color-mode="auto" data-light-theme="light" data-dark-theme="dark" data-darkreader-mode="dynamic" data-darkreader-scheme="dark"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><style class="darkreader darkreader--fallback" media="screen"></style><style class="darkreader darkreader--text" media="screen"></style><style class="darkreader darkreader--invert" media="screen">.jfk-bubble.gtx-bubble, .captcheck_answer_label > input + img, span#closed_text > img[src^="https://www.gstatic.com/images/branding/googlelogo"], span[data-href^="https://www.hcaptcha.com/"] > #icon, #bit-notification-bar-iframe, ::-webkit-calendar-picker-indicator, embed[type="application/pdf"], [src="https://github.githubassets.com/images/modules/site/icons/footer/github-logo.svg"], [src^="https://github.githubassets.com/images/modules/site/home/community-sponsor-"], [src^="https://github.githubassets.com/images/modules/site/home/community-readme-"], [src^="https://github.githubassets.com/images/modules/site/home/community-discussions-"], [src="https://github.githubassets.com/images/modules/site/home/dependabot-merge.png"], [src="https://github.githubassets.com/images/modules/site/home/dependabot-pr.png"], [src="https://github.githubassets.com/images/modules/site/home/gh-desktop.png"], [src="https://github.githubassets.com/images/modules/site/home/pr-merge.png"], [src="https://github.githubassets.com/images/modules/site/home/pr-comment.png"], [src="https://github.githubassets.com/images/modules/site/home/pr-description.png"], [src="https://github.githubassets.com/images/modules/site/home/pr-screen.png"], [src="https://github.githubassets.com/images/modules/site/home/enterprise-city-w-logos.jpg"], [src="https://github.githubassets.com/images/modules/site/codespaces/codespaces-icon.png"], [src="https://github.githubassets.com/images/modules/site/codespaces/dependency-rust.png"], [src="https://github.githubassets.com/images/modules/site/codespaces/dependency-3.png"], [src^="https://github.githubassets.com/images/modules/site/codespaces/dependencies-"], [src="https://github.githubassets.com/images/modules/site/codespaces/commit-3.png"], [src="https://github.githubassets.com/images/modules/site/codespaces/extensions-1.png"], [src="https://github.githubassets.com/images/modules/site/codespaces/extensions-2.png"], [src="https://github.githubassets.com/images/modules/site/codespaces/commit-workflow.png"], [src="https://github.githubassets.com/images/modules/site/codespaces/workflow-view.png"], [src="https://github.githubassets.com/images/modules/site/codespaces/code.png"], [src="https://github.githubassets.com/images/email/explore/explore-gradient-icon.png"], [src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/collections/learn-to-code/learn-to-code.png"], .js-viewport-aware-video.color-bg-primary.width-full.d-block.codespaces-hero-video, .build-in-animate.position-relative.mb-6-fluid.box-shadow-active-mktg.mx-auto.home-mobile-iphone.build-in-slideY.js-build-in > .js-viewport-aware-video.width-full, .overflow-hidden.position-relative.box-shadow-active-border-mktg.rounded-2-fluid.color-bg-primary.build-in-scale-fade.js-build-in-item, .build-in-animate.overflow-hidden.box-shadow-active-border-mktg.rounded-2-fluid.position-relative.home-workflow-comp.js-build-in-item, .mx-lg-auto.col-lg-7.col-12 {
    filter: invert(100%) hue-rotate(180deg) brightness(80%) contrast(90%) sepia(55%) !important;
}</style><style class="darkreader darkreader--inline" media="screen">[data-darkreader-inline-bgcolor] {
  background-color: var(--darkreader-inline-bgcolor) !important;
}
[data-darkreader-inline-bgimage] {
  background-image: var(--darkreader-inline-bgimage) !important;
}
[data-darkreader-inline-border] {
  border-color: var(--darkreader-inline-border) !important;
}
[data-darkreader-inline-border-bottom] {
  border-bottom-color: var(--darkreader-inline-border-bottom) !important;
}
[data-darkreader-inline-border-left] {
  border-left-color: var(--darkreader-inline-border-left) !important;
}
[data-darkreader-inline-border-right] {
  border-right-color: var(--darkreader-inline-border-right) !important;
}
[data-darkreader-inline-border-top] {
  border-top-color: var(--darkreader-inline-border-top) !important;
}
[data-darkreader-inline-boxshadow] {
  box-shadow: var(--darkreader-inline-boxshadow) !important;
}
[data-darkreader-inline-color] {
  color: var(--darkreader-inline-color) !important;
}
[data-darkreader-inline-fill] {
  fill: var(--darkreader-inline-fill) !important;
}
[data-darkreader-inline-stroke] {
  stroke: var(--darkreader-inline-stroke) !important;
}
[data-darkreader-inline-outline] {
  outline-color: var(--darkreader-inline-outline) !important;
}
[data-darkreader-inline-stopcolor] {
  stop-color: var(--darkreader-inline-stopcolor) !important;
}</style><style class="darkreader darkreader--variables" media="screen">:root {
   --darkreader-neutral-background: #131210;
   --darkreader-neutral-text: #ccbda2;
   --darkreader-selection-background: #284059;
   --darkreader-selection-text: #dccdb1;
}</style><style class="darkreader darkreader--root-vars" media="screen"></style><script class="darkreader darkreader--proxy">(function injectProxy() {
        document.dispatchEvent(
            new CustomEvent("__darkreader__inlineScriptsAllowed")
        );
        const addRuleDescriptor = Object.getOwnPropertyDescriptor(
            CSSStyleSheet.prototype,
            "addRule"
        );
        const insertRuleDescriptor = Object.getOwnPropertyDescriptor(
            CSSStyleSheet.prototype,
            "insertRule"
        );
        const deleteRuleDescriptor = Object.getOwnPropertyDescriptor(
            CSSStyleSheet.prototype,
            "deleteRule"
        );
        const removeRuleDescriptor = Object.getOwnPropertyDescriptor(
            CSSStyleSheet.prototype,
            "removeRule"
        );
        const shouldWrapDocStyleSheets =
            location.hostname.endsWith("pushbullet.com") ||
            location.hostname.endsWith("ilsole24ore.com") ||
            location.hostname.endsWith("allegro.pl");
        const documentStyleSheetsDescriptor = shouldWrapDocStyleSheets
            ? Object.getOwnPropertyDescriptor(Document.prototype, "styleSheets")
            : null;
        const cleanUp = () => {
            Object.defineProperty(
                CSSStyleSheet.prototype,
                "addRule",
                addRuleDescriptor
            );
            Object.defineProperty(
                CSSStyleSheet.prototype,
                "insertRule",
                insertRuleDescriptor
            );
            Object.defineProperty(
                CSSStyleSheet.prototype,
                "deleteRule",
                deleteRuleDescriptor
            );
            Object.defineProperty(
                CSSStyleSheet.prototype,
                "removeRule",
                removeRuleDescriptor
            );
            document.removeEventListener("__darkreader__cleanUp", cleanUp);
            document.removeEventListener(
                "__darkreader__addUndefinedResolver",
                addUndefinedResolver
            );
            if (shouldWrapDocStyleSheets) {
                Object.defineProperty(
                    Document.prototype,
                    "styleSheets",
                    documentStyleSheetsDescriptor
                );
            }
        };
        const addUndefinedResolver = (e) => {
            customElements.whenDefined(e.detail.tag).then(() => {
                document.dispatchEvent(
                    new CustomEvent("__darkreader__isDefined", {
                        detail: {tag: e.detail.tag}
                    })
                );
            });
        };
        document.addEventListener("__darkreader__cleanUp", cleanUp);
        document.addEventListener(
            "__darkreader__addUndefinedResolver",
            addUndefinedResolver
        );
        const updateSheetEvent = new Event("__darkreader__updateSheet");
        function proxyAddRule(selector, style, index) {
            addRuleDescriptor.value.call(this, selector, style, index);
            if (
                this.ownerNode &&
                !this.ownerNode.classList.contains("darkreader")
            ) {
                this.ownerNode.dispatchEvent(updateSheetEvent);
            }
            return -1;
        }
        function proxyInsertRule(rule, index) {
            const returnValue = insertRuleDescriptor.value.call(
                this,
                rule,
                index
            );
            if (
                this.ownerNode &&
                !this.ownerNode.classList.contains("darkreader")
            ) {
                this.ownerNode.dispatchEvent(updateSheetEvent);
            }
            return returnValue;
        }
        function proxyDeleteRule(index) {
            deleteRuleDescriptor.value.call(this, index);
            if (
                this.ownerNode &&
                !this.ownerNode.classList.contains("darkreader")
            ) {
                this.ownerNode.dispatchEvent(updateSheetEvent);
            }
        }
        function proxyRemoveRule(index) {
            removeRuleDescriptor.value.call(this, index);
            if (
                this.ownerNode &&
                !this.ownerNode.classList.contains("darkreader")
            ) {
                this.ownerNode.dispatchEvent(updateSheetEvent);
            }
        }
        function proxyDocumentStyleSheets() {
            const docSheets = documentStyleSheetsDescriptor.get.call(this);
            const filtered = [...docSheets].filter((styleSheet) => {
                return !styleSheet.ownerNode.classList.contains("darkreader");
            });
            return Object.setPrototypeOf(filtered, StyleSheetList.prototype);
        }
        Object.defineProperty(
            CSSStyleSheet.prototype,
            "addRule",
            Object.assign({}, addRuleDescriptor, {value: proxyAddRule})
        );
        Object.defineProperty(
            CSSStyleSheet.prototype,
            "insertRule",
            Object.assign({}, insertRuleDescriptor, {value: proxyInsertRule})
        );
        Object.defineProperty(
            CSSStyleSheet.prototype,
            "deleteRule",
            Object.assign({}, deleteRuleDescriptor, {value: proxyDeleteRule})
        );
        Object.defineProperty(
            CSSStyleSheet.prototype,
            "removeRule",
            Object.assign({}, removeRuleDescriptor, {value: proxyRemoveRule})
        );
        if (shouldWrapDocStyleSheets) {
            Object.defineProperty(
                Document.prototype,
                "styleSheets",
                Object.assign({}, documentStyleSheetsDescriptor, {
                    get: proxyDocumentStyleSheets
                })
            );
        }
    })()</script><style class="darkreader darkreader--user-agent" media="screen">html {
    background-color: #181714 !important;
}
html, body, input, textarea, select, button {
    background-color: #181714;
}
html, body, input, textarea, select, button {
    border-color: #695f4e;
    color: #dccdb1;
}
a {
    color: #617b93;
}
table {
    border-color: #535047;
}
::placeholder {
    color: #a69881;
}
input:-webkit-autofill,
textarea:-webkit-autofill,
select:-webkit-autofill {
    background-color: #4c4920 !important;
    color: #dccdb1 !important;
}
::-webkit-scrollbar {
    background-color: #201f1b;
    color: #9f927b;
}
::-webkit-scrollbar-thumb {
    background-color: #44413a;
}
::-webkit-scrollbar-thumb:hover {
    background-color: #565349;
}
::-webkit-scrollbar-thumb:active {
    background-color: #47453d;
}
::-webkit-scrollbar-corner {
    background-color: #181714;
}
::selection {
    background-color: #284059 !important;
    color: #dccdb1 !important;
}
::-moz-selection {
    background-color: #284059 !important;
    color: #dccdb1 !important;
}</style>
    
  <link rel="dns-prefetch" href="https://github.githubassets.com/">
  <link rel="dns-prefetch" href="https://avatars.githubusercontent.com/">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com/">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">



  <link crossorigin="anonymous" media="all" integrity="sha512-J/5cWm5rrVuxkSgldaK1emf5j30Bs5mRgu0uhuHrG+iwf9mD2LOrkQ32SyN5PADLWzkSDxLS3bW/ScsiM44wzw==" rel="stylesheet" href="./sklearn_abalone_featurizer_files/frameworks-27fe5c5a6e6bad5bb191282575a2b57a.css"><style class="darkreader darkreader--sync" media="screen"></style>
  
    <link crossorigin="anonymous" media="all" integrity="sha512-tLF7vl8nbeo3WRDlqIAgYYiEl53NFb2F58kvIEfCYd/Dgq76zXKIhZpEAO9H4wtqaV+0npnvmQF1rjAMq6b1tA==" rel="stylesheet" href="./sklearn_abalone_featurizer_files/behaviors-b4b17bbe5f276dea375910e5a8802061.css"><style class="darkreader darkreader--sync" media="screen"></style>
    
    
    
    <link crossorigin="anonymous" media="all" integrity="sha512-iiK72fBJnLBFZ4awdLtCnik7g77ABo26q8xMdxoPOQgAKqV+hpf1UhKAooJegxIq8c0QADlUsKd63HVPgtRNYw==" rel="stylesheet" href="./sklearn_abalone_featurizer_files/github-8a22bbd9f0499cb0456786b074bb429e.css"><style class="darkreader darkreader--sync" media="screen"></style>

  <script crossorigin="anonymous" defer="defer" integrity="sha512-CzeY4A6TiG4fGZSWZU8FxmzFFmcQFoPpArF0hkH0/J/S7UL4eed/LKEXMQXfTwiG5yEJBI+9BdKG8KQJNbhcIQ==" type="application/javascript" src="./sklearn_abalone_featurizer_files/environment-0b3798e0.js.download"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-czQZrI8Ar39Oil36WxqNfOBo7pZqlK1CUHWZ8CF9jMxyawHGQ+lKiPtd25OvoNHZF69LfWPpafuwqxcfiG/iYA==" type="application/javascript" src="./sklearn_abalone_featurizer_files/chunk-frameworks-733419ac.js.download"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-YOzkTPNBhsGBHTWNXcjLCxYM3ANDGkp2gejU1oLAxIG4g8VAZJlFYJX2Eo//GCdStAeiby9Y2FecMxmDQwj+Ow==" type="application/javascript" src="./sklearn_abalone_featurizer_files/chunk-vendor-60ece44c.js.download"></script>
  
  <script crossorigin="anonymous" defer="defer" integrity="sha512-U5w2SuNhe024Q+iVhaZ18HiQCUlgfujDoHEjt9JRP0MRtF4TUhuBd/Ur2yIsgVsM0Q1GSS7yDokYo8unl+F3JQ==" type="application/javascript" src="./sklearn_abalone_featurizer_files/behaviors-539c364a.js.download"></script>
  
    <script crossorigin="anonymous" defer="defer" integrity="sha512-5tWKSr7mhAzSh4Sx5YRFgKftdGxKwHKnOGYw5DlxjHhkQVURYFU3Bk5IMOGMKuAiJTlC3OXYM3xzGcyjzuEFQQ==" type="application/javascript" data-module-id="./chunk-animate-on-scroll.js" data-src="https://github.githubassets.com/assets/chunk-animate-on-scroll-e6d58a4a.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-0MZorw3oXnKy5eeSwQ9xGrKU4hxQeCXxmyxhneIHNhDIqu8vWh8mHss9FlC75Xd/bPWxFDCvdOo57tnTR46nbA==" type="application/javascript" data-module-id="./chunk-codemirror.js" data-src="https://github.githubassets.com/assets/chunk-codemirror-d0c668af.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-M6W/sGLOuJXCIkw+doDl6zl7J9q2DmqdwftQCtyEiZM/UJNGRVQdyKwI/PAMxD12se/wCx3ZcyJs9nz0o0OSVw==" type="application/javascript" data-module-id="./chunk-color-modes.js" src="./sklearn_abalone_featurizer_files/chunk-color-modes-33a5bfb0.js.download"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-71HZu1T5JWqRNF9wrm2NXZAqYVvzxZ8Dvor5U5l/LuEBbGCBX57Sny60Rj+qUZZAvEBGFlNsz179DEn2HFwgVA==" type="application/javascript" data-module-id="./chunk-confetti.js" data-src="https://github.githubassets.com/assets/chunk-confetti-ef51d9bb.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-P29U0lNmhUj353VrCWp6czdhNpMtF70xVKf4GBGFVKCoqGtxp0sywAM8/46+iC0kdFiRvM13EBvDnq6oyWRwiw==" type="application/javascript" data-module-id="./chunk-contributions-spider-graph.js" data-src="https://github.githubassets.com/assets/chunk-contributions-spider-graph-3f6f54d2.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-6j/oSF+kbW+yetNPvI684VzAu9pzug6Vj2h+3u1LdCuRhR4jnuiHZfeQKls3nxcT/S3H+oIt7FtigE/aeoj+gg==" type="application/javascript" data-module-id="./chunk-drag-drop.js" data-src="https://github.githubassets.com/assets/chunk-drag-drop-ea3fe848.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-VSSd+Yzi2iMS+pibY6hD/WdypxAEdob5F2RMKxuKcAHS2EpFYJPeTXoVxt0NXg03tfj2dka2mEtHS+vjpYSaDw==" type="application/javascript" data-module-id="./chunk-edit-hook-secret-element.js" data-src="https://github.githubassets.com/assets/chunk-edit-hook-secret-element-55249df9.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-XObZgIojqwx94ekra728uVPTHs30O37w4+dNCDNUrZXRnGmFRcitdymWoSEm7ztcvhzboxHmXOSP2TeoPSfQ5Q==" type="application/javascript" data-module-id="./chunk-edit.js" src="./sklearn_abalone_featurizer_files/chunk-edit-5ce6d980.js.download"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-aiqMIGGZGo8AQMjcoImKPMTsZVVRl6htCSY7BpRmpGPG/AF+Wq+P/Oj/dthWQOIk9cCNMPEas7O2zAR6oqn0tA==" type="application/javascript" data-module-id="./chunk-emoji-picker-element.js" data-src="https://github.githubassets.com/assets/chunk-emoji-picker-element-6a2a8c20.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-qqRgtYe+VBe9oQvKTYSA9uVb3qCKhEMl3sHdsnP8AbVRfumjSOugTCEN1YLmnniNBMXb77ty2wddblbKSaQE1Q==" type="application/javascript" data-module-id="./chunk-failbot.js" src="./sklearn_abalone_featurizer_files/chunk-failbot-aaa460b5.js.download"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-YrRWJ3DBTEGQ3kU5vH0Btt+bjUcZHoTj66uIO7wFIfT1LoKJQ0Q2+UTn4rmeKn+PrnMAnQogCNC6Lka17tDncw==" type="application/javascript" data-module-id="./chunk-filter-input.js" data-src="https://github.githubassets.com/assets/chunk-filter-input-62b45627.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-Z1wcyOFQHzyMSPqp5DLKrobr3DN2Q6Dz31cfPtw4b2vPs9PX0PrxyDXHpTbIlcZ9qT1M1BNAypHKKw8Lp6Yx/Q==" type="application/javascript" data-module-id="./chunk-insights-graph.js" data-src="https://github.githubassets.com/assets/chunk-insights-graph-675c1cc8.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-gwtCVvmTqprGdoOWD5qAo64uilYKmDOqEN0XIzMX9KT9u8HabjeF9sk/819qZEcUAZbpzd7gNOU7YW0CDkaEjg==" type="application/javascript" data-module-id="./chunk-insights-query.js" data-src="https://github.githubassets.com/assets/chunk-insights-query-830b4256.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-lmosGyye+/xONUQs9SwGN/a9fQvUSiAFk5HrL8eLHjeuOx9DX9TW5ckRKFD+6FM54vutFf/mBmNFW/0R3KJEBw==" type="application/javascript" data-module-id="./chunk-invitations.js" data-src="https://github.githubassets.com/assets/chunk-invitations-966a2c1b.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-4MxGQhsDODvZgLbu5arO6CapfnNvZ5fXMsZ47FiklUKRmHq4B3h8uTokSIWAOAxsvCMRrZr0DVZ0i0gm3RAnsg==" type="application/javascript" data-module-id="./chunk-jump-to.js" data-src="https://github.githubassets.com/assets/chunk-jump-to-e0cc4642.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-VtdawM/OSsu+d6v25ZY6UcQa/GGLAStSESjsqdEwx+ey88GNYGkQ24o+JFFo4lY+7wLMRf7aCrLxkA5SquBoNQ==" type="application/javascript" data-module-id="./chunk-launch-code-element.js" data-src="https://github.githubassets.com/assets/chunk-launch-code-element-56d75ac0.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-RduaLAviB2ygvRK/eX5iwzYO43ie7svrJ0rYJs06x7XqpRl/IK8PPBscBWM9Moo5Z86DK2iRLE2+aR7TJ5Uc2Q==" type="application/javascript" data-module-id="./chunk-metric-selection-element.js" data-src="https://github.githubassets.com/assets/chunk-metric-selection-element-45db9a2c.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-7hZ031ngiF36wGsfcoyyCWTqwYxjX+qeTLtCV7CJ+IO+wzkzCm1RoR3WzWczfWmwLNqr+Hu3kQOgkBaGn4ntWQ==" type="application/javascript" data-module-id="./chunk-notification-list-focus.js" src="./sklearn_abalone_featurizer_files/chunk-notification-list-focus-ee1674df.js.download"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-ma0OOy3nj0c1cqBx0BkcmIFsLqcSZ+MIukQxyEFM/OWTzZpG+QMgOoWPAHZz43M6fyjAUG1jH6c/6LPiiKPCyw==" type="application/javascript" data-module-id="./chunk-profile-pins-element.js" data-src="https://github.githubassets.com/assets/chunk-profile-pins-element-99ad0e3b.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-hgoSKLTlL8I3IWr/TLONCU+N4kdCtdrHCrrud4NKhgRlLrTw0XUPhqBaDdZUiFSzDQRw/nFQ1kw2VeTm0g9+lA==" type="application/javascript" data-module-id="./chunk-profile.js" data-src="https://github.githubassets.com/assets/chunk-profile-860a1228.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-dmP0pnRItCP7ydEXVipp98lz/HaQtHyG00kfd8lMS5AoLbDwGfqXPjj7Q0qLGpPc7lBkySNNHIeEPF7NblctEA==" type="application/javascript" data-module-id="./chunk-readme-toc-element.js" data-src="https://github.githubassets.com/assets/chunk-readme-toc-element-7663f4a6.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-/fwTpG2i+GCgHEZc/35F+pXdShv1RfJMxyixcTIxzxDdylOWVJvjIWoumYWEPj7gUqBdrWt4SFf989Szmxleaw==" type="application/javascript" data-module-id="./chunk-ref-selector.js" src="./sklearn_abalone_featurizer_files/chunk-ref-selector-fdfc13a4.js.download"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-D/MxBjtRPjes6DvnYGi2dEH7AQEnLvSvTODabEkSo+1zP6SSEZpb8oF52kFWERA97t1L19fF/P3bn4pgIsMPuA==" type="application/javascript" data-module-id="./chunk-responsive-underlinenav.js" src="./sklearn_abalone_featurizer_files/chunk-responsive-underlinenav-0ff33106.js.download"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-SWy36S28Js+/YzsvYgmp+IEdC0qtMcBf6sYhXTEcj1aFPCLPOTOnOKqzFiNyH2oNVDd+u5Qi8eqYINSIu28LFQ==" type="application/javascript" data-module-id="./chunk-runner-groups.js" data-src="https://github.githubassets.com/assets/chunk-runner-groups-496cb7e9.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-FcH835sK5dmHJmGX2K6Vp4tFq7gUEykUvVXTf+7LmdLoLuYjxIGixOfLxBeCQ+1LDTJ/43bSgqmlDlN0qnGTYQ==" type="application/javascript" data-module-id="./chunk-series-table.js" data-src="https://github.githubassets.com/assets/chunk-series-table-15c1fcdf.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-tk76eoSLUqXSVZ8ANzPprrOImFIV1zQ/VBV+WzG8ZjZpVPH8cLkMH/ur5HJB1lxx9/yo+V2wjDF96t4qfUwZLA==" type="application/javascript" data-module-id="./chunk-severity-calculator-element.js" data-src="https://github.githubassets.com/assets/chunk-severity-calculator-element-b64efa7a.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-j7Pb1H+2Xt4YIKSrJLLXxl/NNkkpW//5PLTpu58JGD8pqRPODDjJKqjO6YPZd++BB4VJubHPjzvuMXhW/9jcqA==" type="application/javascript" data-module-id="./chunk-sortable-behavior.js" data-src="https://github.githubassets.com/assets/chunk-sortable-behavior-8fb3dbd4.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-nKa3UdA2O7Ve4Jn24gaB20yUfJvS7wlnd8Q8C+iWD8i2tXLgaKemDWkLeexeQdrs+an98FCl5fOiy0J+izn+tQ==" type="application/javascript" data-module-id="./chunk-three.module.js" data-src="https://github.githubassets.com/assets/chunk-three.module-9ca6b751.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-WK8VXw3lfUQ/VRW0zlgKPhcMUqH0uTnB/KzePUPdZhCm/HpxfXXHKTGvj5C0Oex7+zbIM2ECzULbtTCT4ug3yg==" type="application/javascript" data-module-id="./chunk-toast.js" data-src="https://github.githubassets.com/assets/chunk-toast-58af155f.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-1vSZvwpr106s8wjSNFNFGVmFT2E4YjI2N8k6JqiSb28GGYMkEJUhveotmvB00Z4bQZM61ZgvWcXax1U3M48gLQ==" type="application/javascript" data-module-id="./chunk-tweetsodium.js" data-src="https://github.githubassets.com/assets/chunk-tweetsodium-d6f499bf.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-UOFNW/xcxynplVfC8Y3fQdFFiasmugYUUHU4N90G8sqBZGL1yR37yjVakxV8/FV5deBALx9OQMBoiba/3OHGDA==" type="application/javascript" data-module-id="./chunk-user-status-submit.js" data-src="https://github.githubassets.com/assets/chunk-user-status-submit-50e14d5b.js"></script>
    <script crossorigin="anonymous" defer="defer" integrity="sha512-cKu/+X7gT+WVH4sXKt0g3G77bfQfcgwurRObM+dt8XylPm9eEWI+/aWKhVab6VsYuvvuI5BTriKXhXfJwaSXdQ==" type="application/javascript" data-module-id="./chunk-webgl-warp.js" data-src="https://github.githubassets.com/assets/chunk-webgl-warp-70abbff9.js"></script>
  
  <script crossorigin="anonymous" defer="defer" integrity="sha512-Sdymqck/Db6vBzsxPsblUmIoMPKtR1aaHLuoRG/YAFKsNxNDN7KZ9er+s/+Ajs5hvScy8gP5T1TVU1u+eLtybA==" type="application/javascript" src="./sklearn_abalone_featurizer_files/codespaces-49dca6a9.js.download"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-9Ux7Idk4v6NfGWWacPgVOXymjG/0NapCoK352oWRQAb6yzpMuh4dfmo33HNbxQytH00P1bmOScD2Z3KZwJMS1Q==" type="application/javascript" src="./sklearn_abalone_featurizer_files/repositories-f54c7b21.js.download"></script>
<script crossorigin="anonymous" defer="defer" integrity="sha512-E8U8knz112xo09iJevWlgrHpfkqgqE3pMeFAgbqGiICeDLM928ko2PBFoJ74sIMHKdOvoeACKCGi/Dimyf1xGg==" type="application/javascript" src="./sklearn_abalone_featurizer_files/topic-suggestions-13c53c92.js.download"></script>

  <meta name="viewport" content="width=device-width">
  
  <title>amazon-sagemaker-examples/sklearn_abalone_featurizer.py at master · aws/amazon-sagemaker-examples · GitHub</title>
    <meta name="description" content="Example 📓 Jupyter notebooks that demonstrate how to build, train, and deploy machine learning models using 🧠 Amazon SageMaker.  - aws/amazon-sagemaker-examples">
    <link rel="search" type="application/opensearchdescription+xml" href="https://github.com/opensearch.xml" title="GitHub">
  <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
  <meta property="fb:app_id" content="1401488693436528">
  <meta name="apple-itunes-app" content="app-id=1477376905">
    <meta name="twitter:image:src" content="https://opengraph.githubassets.com/94c0cfc29379552dbee414bec7004424c7a2457f7175bb6fc4c72c696eb22b22/aws/amazon-sagemaker-examples"><meta name="twitter:site" content="@github"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="aws/amazon-sagemaker-examples"><meta name="twitter:description" content="Example 📓 Jupyter notebooks that demonstrate how to build, train, and deploy machine learning models using 🧠 Amazon SageMaker.  - aws/amazon-sagemaker-examples">
    <meta property="og:image" content="https://opengraph.githubassets.com/94c0cfc29379552dbee414bec7004424c7a2457f7175bb6fc4c72c696eb22b22/aws/amazon-sagemaker-examples"><meta property="og:image:alt" content="Example 📓 Jupyter notebooks that demonstrate how to build, train, and deploy machine learning models using 🧠 Amazon SageMaker.  - aws/amazon-sagemaker-examples"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="600"><meta property="og:site_name" content="GitHub"><meta property="og:type" content="object"><meta property="og:title" content="aws/amazon-sagemaker-examples"><meta property="og:url" content="https://github.com/aws/amazon-sagemaker-examples"><meta property="og:description" content="Example 📓 Jupyter notebooks that demonstrate how to build, train, and deploy machine learning models using 🧠 Amazon SageMaker.  - aws/amazon-sagemaker-examples">



    

  <link rel="assets" href="https://github.githubassets.com/">
  

  

    


  

  

  

    <meta name="google-site-verification" content="c1kuD-K2HIVF635lypcsWPoD4kilo5-jA_wBFyT4uMY">
  <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
  <meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
  <meta name="google-site-verification" content="GXs5KoUUkNCoaAZn7wPN-t01Pywp9M3sEjnt_3_ZWPc">

  <meta name="octolytics-host" content="collector.githubapp.com"><meta name="octolytics-app-id" content="github"><meta name="octolytics-event-url" content="https://collector.githubapp.com/github-external/browser_event">

  

  






  

      <meta name="hostname" content="github.com">
    <meta name="user-login" content="">


      <meta name="expected-hostname" content="github.com">


    <meta name="enabled-features" content="MARKETPLACE_PENDING_INSTALLATIONS">

  <meta http-equiv="x-pjax-version" content="8351ab5c35a463f4e719f57f98aa1d5d0c7275567ae178e276431c3f498414cc">
  

    
  <meta name="go-import" content="github.com/aws/amazon-sagemaker-examples git https://github.com/aws/amazon-sagemaker-examples.git">

  <meta name="octolytics-dimension-user_id" content="2232217"><meta name="octolytics-dimension-user_login" content="aws"><meta name="octolytics-dimension-repository_id" content="107937815"><meta name="octolytics-dimension-repository_nwo" content="aws/amazon-sagemaker-examples"><meta name="octolytics-dimension-repository_public" content="true"><meta name="octolytics-dimension-repository_is_fork" content="false"><meta name="octolytics-dimension-repository_network_root_id" content="107937815"><meta name="octolytics-dimension-repository_network_root_nwo" content="aws/amazon-sagemaker-examples">



    


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <meta name="browser-optimizely-client-errors-url" content="https://api.github.com/_private/browser/optimizely_client/errors">

  <link rel="mask-icon" href="https://github.githubassets.com/pinned-octocat.svg" color="#000000" data-darkreader-inline-color="" style="--darkreader-inline-color:#dccdb1;">
  <link rel="alternate icon" class="js-site-favicon" type="image/png" href="https://github.githubassets.com/favicons/favicon-dark.png">
  <link rel="icon" class="js-site-favicon" type="image/svg+xml" href="https://github.githubassets.com/favicons/favicon-dark.svg">

<meta name="theme-color" content="#191916">
<meta name="color-scheme" content="light dark">

  <meta name="msapplication-TileImage" content="/windows-tile.png">
  <meta name="msapplication-TileColor" content="#ffffff">

  <link rel="manifest" href="https://github.com/manifest.json" crossorigin="use-credentials">

<meta name="enabled-homepage-translation-languages" content="">

  <meta name="darkreader" content="cc8882066234bfe124713dfb35cbe72b"><style class="darkreader darkreader--override" media="screen">.vimvixen-hint {
    background-color: #5c4819 !important;
    border-color: #b0974b !important;
    color: #e1cea7 !important;
}
::placeholder {
    opacity: 0.5 !important;
}
a[href="https://coinmarketcap.com/"] > svg[width="94"][height="16"] > path {
    fill: var(--darkreader-neutral-text) !important;
}
#edge-translate-panel-body {
    color: var(--darkreader-neutral-text) !important;
}
.markdown-body code,
.markdown-body pre,
.markdown-title code {
    background-color: rgba(212, 199, 174, 0.1) !important;
}
.markdown-body pre code {
    background-color: transparent !important;
}
.refined-github .dashboard .js-all-activity-header + div {
    background-color: #161514 !important;
    border-color: #373531 !important;
}
.refined-github .dashboard-rollup-items .body {
    border-top-color: #373531 !important;
}
.refined-github .reaction-summary-item a {
    box-shadow: 0 0 0 2px #000000 !important;
}
.refined-github button.reaction-summary-item {
    border-top-color: rgb(52, 59, 68) !important;
    border-bottom: rgb(77, 172, 253) !important;
}
.js-site-search-form {
    background-color: #ffffff1a !important;
    border-radius: 2pt !important;
}
.blob-num:not(.cc-coverage-covered-border):not(.cc-coverage-missed-border) {
    border-right: 0 !important;
}
.cc-issue-description {
    color: #24292e !important;
}
.cc-readup-background {
    background-color: rgb(28, 30, 31) !important
}
.cc-readup-content {
    border-left: 1px solid grey !important;
    color: rgb(216, 214, 208) !important;
}
.cc-readup-content blockquote {
    border-left: 3px solid dimgrey !important;
}
.cc-pr__link-text {
    color: darkgrey !important;
}
.cc-pr__tooltip {
    background-color: rgb(28, 30, 31) !important;
    color: darkgrey !important;
}
.jfk-bubble, .octotree-sidebar, .cc-pr__logo, .cc-octicon, #network canvas, img.network-tree {
    filter: invert(94.4%) hue-rotate(180deg) contrast(90%) !important;
}
.blob-code-inner, .blob-code-inner > *, .CodeMirror pre > span, .CodeMirror-linenumber {
    font-family: SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace !important;
}
#commit-activity-detail > svg {
    fill: #f3e3c5 !important;
}
.ContributionCalendar-day,
.ContributionCalendar-day[data-level="0"] {
    fill: var(--color-calendar-graph-day-bg) !important;
}
.ContributionCalendar-day[data-level="1"] {
    fill: var(--color-calendar-graph-day-L1-bg) !important;
}
.ContributionCalendar-day[data-level="2"] {
    fill: var(--color-calendar-graph-day-L2-bg) !important;
}
.ContributionCalendar-day[data-level="3"] {
    fill: var(--color-calendar-graph-day-L3-bg) !important;
}
.ContributionCalendar-day[data-level="4"] {
    fill: var(--color-calendar-graph-day-L4-bg) !important;
}
.day,
.day[data-Count="0"] {
    fill: var(--color-calendar-graph-day-bg) !important;
}
.day[data-Count="1"] {
    fill: var(--color-calendar-graph-day-L1-bg) !important;
}
.day[data-Count="2"] {
    fill: var(--color-calendar-graph-day-L2-bg) !important;
}
.day[data-Count="3"] {
    fill: var(--color-calendar-graph-day-L3-bg) !important;
}
.day[data-Count="4"] {
    fill: var(--color-calendar-graph-day-L4-bg) !important;
}
:root {
    --color-previewable-comment-form-bg: var(--darkreader-neutral-background) !important;
    --color-calendar-graph-day-bg: #100f0e !important;
    --color-calendar-graph-day-L1-bg: #415736 !important;
    --color-calendar-graph-day-L2-bg: #7ba16b !important;
    --color-calendar-graph-day-L3-bg: #93b07d !important;
    --color-calendar-graph-day-L4-bg: #b0be94 !important;
}
.Box-row--yellow {
    background-color: #141104 !important;
}
.merge-status-list {
    border-color: #37352e !important;
}
.user-has-reacted {
    background-color: rgba(17, 88, 199, 0.2) !important;
}
.hx_IssueLabel {
    background: rgb(var(--label-r),var(--label-g),var(--label-b)) !important;
    color: hsl(0,0%,calc(var(--lightness-switch)*100%)) !important;
    border-color: hsla(var(--label-h),calc(var(--label-s)*1%),calc((var(--label-l) - 25)*1%),var(--border-alpha)) !important;
}
.header-search-input {
    border: 0 !important;
}
.timeline-comment--caret.current-user::after {
    --color-current-user-tip-bg: var(--darkreader-bg--color-box-bg-info) !important;
}
.timeline-comment--caret.current-user::before {
    background-color: var(--darkreader-border--color-box-border-info) !important;
}
@media screen and (min-width: 1012px) {
    markdown-toolbar.border-lg-top-0 {
        border-top: 1px solid var(--darkreader-border--color-border-primary) !important;
    }
}
@media screen and (max-width: 767px) {
    div.tabnav--responsive button.tabnav-tab {
        --color-border-primary: var(--darkreader-border--color-border-primary) !important;
    }
}
.TimelineItem-badge[style^="background-color: var(--color-timeline-merged-bg)"] {
    background-color: var(--color-timeline-merged-bg) !important;
}
.ContributionCalendar-label {
    --color-text-primary: var(--darkreader-neutral-text) !important;
}
article div[style^="background: linear-gradient"] {
    background: linear-gradient(to top, var(--darkreader-bg--color-bg-primary), transparent) !important;
}</style><meta name="selected-link" value="repo_source" data-pjax-transient=""><meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient=""><meta name="request-id" content="1EB9:0148:D215C:16B806:60E69BA4" data-pjax-transient=""><meta name="html-safe-nonce" content="3a46874efffb743807b87d8912a6031175db0be69ef816eb59920512655503f4" data-pjax-transient=""><meta name="visitor-payload" content="eyJyZWZlcnJlciI6Imh0dHBzOi8vZ2l0aHViLmNvbS9hd3MvYW1hem9uLXNhZ2VtYWtlci1leGFtcGxlcy9ibG9iL21hc3Rlci9zYWdlbWFrZXItcHl0aG9uLXNkay9zY2lraXRfbGVhcm5faW5mZXJlbmNlX3BpcGVsaW5lL3NrbGVhcm5fYWJhbG9uZV9mZWF0dXJpemVyLnB5IiwicmVxdWVzdF9pZCI6IjFFQjk6MDE0ODpEMjE1QzoxNkI4MDY6NjBFNjlCQTQiLCJ2aXNpdG9yX2lkIjoiNjYxMDIzNjI5NTQ2NTQ0ODEzNyIsInJlZ2lvbl9lZGdlIjoiYXAtbm9ydGhlYXN0LTEiLCJyZWdpb25fcmVuZGVyIjoiYXAtbm9ydGhlYXN0LTEifQ==" data-pjax-transient=""><meta name="visitor-hmac" content="f9523f477bef79f165e7a7fe172a6c66b45e3632c18d643e7369fbd0e704cc51" data-pjax-transient=""><meta name="github-keyboard-shortcuts" content="repository,source-code" data-pjax-transient=""><meta name="hovercard-subject-tag" content="repository:107937815" data-pjax-transient=""><link rel="canonical" href="https://github.com/aws/amazon-sagemaker-examples/blob/master/sagemaker-python-sdk/scikit_learn_inference_pipeline/sklearn_abalone_featurizer.py" data-pjax-transient=""><script type="application/javascript" src="./sklearn_abalone_featurizer_files/diffs-b529d4b1.js.download"></script></head>

  <body class="logged-out env-production page-responsive intent-mouse" style="word-wrap: break-word;" data-new-gr-c-s-loaded="14.988.0">
    

    <div class="position-relative js-header-wrapper ">
      <a href="https://github.com/aws/amazon-sagemaker-examples/blob/master/sagemaker-python-sdk/scikit_learn_inference_pipeline/sklearn_abalone_featurizer.py#start-of-content" class="px-2 py-4 color-bg-info-inverse color-text-white show-on-focus js-skip-to-content">Skip to content</a>
      <span data-view-component="true" class="progress-pjax-loader width-full js-pjax-loader-bar Progress position-fixed">
    <span style="background-color: rgb(121, 184, 255); width: 100%; --darkreader-inline-bgcolor:#203345; transition: width 0.4s ease 0s;" data-view-component="true" class="Progress-item progress-pjax-loader-bar" data-darkreader-inline-bgcolor=""></span>
</span>      
      


        
            <header class="Header-old header-logged-out js-details-container Details position-relative f4 py-2" role="banner">
  <div class="container-xl d-lg-flex flex-items-center p-responsive">
    <div class="d-flex flex-justify-between flex-items-center">
        <a class="mr-4" href="https://github.com/" aria-label="Homepage" data-ga-click="(Logged out) Header, go to homepage, icon:logo-wordmark">
          <svg height="32" class="octicon octicon-mark-github color-text-white" viewBox="0 0 16 16" version="1.1" width="32" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path></svg>
        </a>

          <div class="d-lg-none css-truncate css-truncate-target width-fit p-2">
            

          </div>

        <div class="d-flex flex-items-center">
              <a href="https://github.com/signup?ref_cta=Sign+up&amp;ref_loc=header+logged+out&amp;ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E%2Ffiles%2Fdisambiguate&amp;source=header-repo" class="d-inline-block d-lg-none f5 color-text-white no-underline border color-border-tertiary rounded-2 px-2 py-1 mr-3 mr-sm-5" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;site header&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;SIGN_UP&quot;,&quot;originating_url&quot;:&quot;https://github.com/aws/amazon-sagemaker-examples/tree/master/sagemaker-python-sdk/scikit_learn_inference_pipeline&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="703021074d188b5ba2e29e151d53d2a5e20a29fb40b77a1fd3dd4535e1dbc387">
                Sign&nbsp;up
              </a>

          <button class="btn-link d-lg-none mt-1 js-details-target" type="button" aria-label="Toggle navigation" aria-expanded="false">
            <svg height="24" class="octicon octicon-three-bars color-text-white" viewBox="0 0 16 16" version="1.1" width="24" aria-hidden="true"><path fill-rule="evenodd" d="M1 2.75A.75.75 0 011.75 2h12.5a.75.75 0 110 1.5H1.75A.75.75 0 011 2.75zm0 5A.75.75 0 011.75 7h12.5a.75.75 0 110 1.5H1.75A.75.75 0 011 7.75zM1.75 12a.75.75 0 100 1.5h12.5a.75.75 0 100-1.5H1.75z"></path></svg>
          </button>
        </div>
    </div>

    <div class="HeaderMenu HeaderMenu--logged-out position-fixed top-0 right-0 bottom-0 height-fit position-lg-relative d-lg-flex flex-justify-between flex-items-center flex-auto">
      <div class="d-flex d-lg-none flex-justify-end border-bottom color-bg-secondary p-3">
        <button class="btn-link js-details-target" type="button" aria-label="Toggle navigation" aria-expanded="false">
          <svg height="24" class="octicon octicon-x color-text-secondary" viewBox="0 0 24 24" version="1.1" width="24" aria-hidden="true"><path fill-rule="evenodd" d="M5.72 5.72a.75.75 0 011.06 0L12 10.94l5.22-5.22a.75.75 0 111.06 1.06L13.06 12l5.22 5.22a.75.75 0 11-1.06 1.06L12 13.06l-5.22 5.22a.75.75 0 01-1.06-1.06L10.94 12 5.72 6.78a.75.75 0 010-1.06z"></path></svg>
        </button>
      </div>

        <nav class="mt-0 px-3 px-lg-0 mb-5 mb-lg-0" aria-label="Global">
          <ul class="d-lg-flex list-style-none">
              <li class="d-block d-lg-flex flex-lg-nowrap flex-lg-items-center border-bottom border-lg-bottom-0 mr-0 mr-lg-3 edge-item-fix position-relative flex-wrap flex-justify-between d-flex flex-items-center ">
                <details class="HeaderMenu-details details-overlay details-reset width-full">
                  <summary class="HeaderMenu-summary HeaderMenu-link px-0 py-3 border-0 no-wrap d-block d-lg-inline-block">
                    Why GitHub?
                    <svg x="0px" y="0px" viewBox="0 0 14 8" xml:space="preserve" fill="none" class="icon-chevon-down-mktg position-absolute position-lg-relative" data-darkreader-inline-fill="" style="--darkreader-inline-fill:none;">
                      <path d="M1,1l6.2,6L13,1"></path>
                    </svg>
                  </summary>
                  <div class="dropdown-menu flex-auto rounded px-0 mt-0 pb-4 p-lg-4 position-relative position-lg-absolute left-0 left-lg-n4">
                    <a href="https://github.com/features" class="py-2 lh-condensed-ultra d-block Link--primary no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Features">Features <span class="Bump-link-symbol float-right text-normal color-text-tertiary pr-3">→</span></a>
                    <ul class="list-style-none f5 pb-3">


                          <li class="edge-item-fix"><a href="https://github.com/mobile" class="py-2 lh-condensed-ultra d-block Link--secondary no-underline f5 Bump-link--hover">Mobile <span class="Bump-link-symbol float-right text-normal color-text-tertiary pr-3">→</span></a></li>
                          <li class="edge-item-fix"><a href="https://github.com/features/actions" class="py-2 lh-condensed-ultra d-block Link--secondary no-underline f5 Bump-link--hover">Actions <span class="Bump-link-symbol float-right text-normal color-text-tertiary pr-3">→</span></a></li>
                          <li class="edge-item-fix"><a href="https://github.com/features/codespaces" class="py-2 lh-condensed-ultra d-block Link--secondary no-underline f5 Bump-link--hover">Codespaces <span class="Bump-link-symbol float-right text-normal color-text-tertiary pr-3">→</span></a></li>
                          <li class="edge-item-fix"><a href="https://github.com/features/packages" class="py-2 lh-condensed-ultra d-block Link--secondary no-underline f5 Bump-link--hover">Packages <span class="Bump-link-symbol float-right text-normal color-text-tertiary pr-3">→</span></a></li>
                          <li class="edge-item-fix"><a href="https://github.com/features/security" class="py-2 lh-condensed-ultra d-block Link--secondary no-underline f5 Bump-link--hover">Security <span class="Bump-link-symbol float-right text-normal color-text-tertiary pr-3">→</span></a></li>
                          <li class="edge-item-fix"><a href="https://github.com/features/code-review/" class="py-2 lh-condensed-ultra d-block Link--secondary no-underline f5 Bump-link--hover">Code review <span class="Bump-link-symbol float-right text-normal color-text-tertiary pr-3">→</span></a></li>
                          <li class="edge-item-fix"><a href="https://github.com/features/issues/" class="py-2 lh-condensed-ultra d-block Link--secondary no-underline f5 Bump-link--hover">Issues <span class="Bump-link-symbol float-right text-normal color-text-tertiary pr-3">→</span></a></li>
                          <li class="edge-item-fix"><a href="https://github.com/features/integrations" class="py-2 lh-condensed-ultra d-block Link--secondary no-underline f5 Bump-link--hover">Integrations <span class="Bump-link-symbol float-right text-normal color-text-tertiary pr-3">→</span></a></li>


                    </ul>

                    <ul class="list-style-none mb-0 border-lg-top pt-lg-3">
                      <li class="edge-item-fix"><a href="https://github.com/sponsors" class="py-2 lh-condensed-ultra d-block no-underline Link--primary no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Sponsors">GitHub Sponsors <span class="Bump-link-symbol float-right text-normal color-text-tertiary pr-3">→</span></a></li>
                      <li class="edge-item-fix"><a href="https://github.com/customer-stories" class="py-2 lh-condensed-ultra d-block no-underline Link--primary no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Customer stories">Customer stories<span class="Bump-link-symbol float-right text-normal color-text-tertiary pr-3">→</span></a></li>
                    </ul>
                  </div>
                </details>
              </li>
              <li class="border-bottom border-lg-bottom-0 mr-0 mr-lg-3">
                <a href="https://github.com/team" class="HeaderMenu-link no-underline py-3 d-block d-lg-inline-block" data-ga-click="(Logged out) Header, go to Team">Team</a>
              </li>
              <li class="border-bottom border-lg-bottom-0 mr-0 mr-lg-3">
                <a href="https://github.com/enterprise" class="HeaderMenu-link no-underline py-3 d-block d-lg-inline-block" data-ga-click="(Logged out) Header, go to Enterprise">Enterprise</a>
              </li>

              <li class="d-block d-lg-flex flex-lg-nowrap flex-lg-items-center border-bottom border-lg-bottom-0 mr-0 mr-lg-3 edge-item-fix position-relative flex-wrap flex-justify-between d-flex flex-items-center ">
                <details class="HeaderMenu-details details-overlay details-reset width-full">
                  <summary class="HeaderMenu-summary HeaderMenu-link px-0 py-3 border-0 no-wrap d-block d-lg-inline-block">
                    Explore
                    <svg x="0px" y="0px" viewBox="0 0 14 8" xml:space="preserve" fill="none" class="icon-chevon-down-mktg position-absolute position-lg-relative" data-darkreader-inline-fill="" style="--darkreader-inline-fill:none;">
                      <path d="M1,1l6.2,6L13,1"></path>
                    </svg>
                  </summary>

                  <div class="dropdown-menu flex-auto rounded px-0 pt-2 pb-0 mt-0 pb-4 p-lg-4 position-relative position-lg-absolute left-0 left-lg-n4">
                    <ul class="list-style-none mb-3">
                      <li class="edge-item-fix"><a href="https://github.com/explore" class="py-2 lh-condensed-ultra d-block Link--primary no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Explore">Explore GitHub <span class="Bump-link-symbol float-right text-normal color-text-tertiary pr-3">→</span></a></li>
                    </ul>

                    <h4 class="color-text-tertiary text-normal text-mono f5 mb-2 border-lg-top pt-lg-3">Learn and contribute</h4>
                    <ul class="list-style-none mb-3">
                      <li class="edge-item-fix"><a href="https://github.com/topics" class="py-2 lh-condensed-ultra d-block Link--secondary no-underline f5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Topics">Topics <span class="Bump-link-symbol float-right text-normal color-text-tertiary pr-3">→</span></a></li>
                        <li class="edge-item-fix"><a href="https://github.com/collections" class="py-2 lh-condensed-ultra d-block Link--secondary no-underline f5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Collections">Collections <span class="Bump-link-symbol float-right text-normal color-text-tertiary pr-3">→</span></a></li>
                      <li class="edge-item-fix"><a href="https://github.com/trending" class="py-2 lh-condensed-ultra d-block Link--secondary no-underline f5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Trending">Trending <span class="Bump-link-symbol float-right text-normal color-text-tertiary pr-3">→</span></a></li>
                      <li class="edge-item-fix"><a href="https://lab.github.com/" class="py-2 lh-condensed-ultra d-block Link--secondary no-underline f5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Learning lab">Learning Lab <span class="Bump-link-symbol float-right text-normal color-text-tertiary pr-3">→</span></a></li>
                      <li class="edge-item-fix"><a href="https://opensource.guide/" class="py-2 lh-condensed-ultra d-block Link--secondary no-underline f5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Open source guides">Open source guides <span class="Bump-link-symbol float-right text-normal color-text-tertiary pr-3">→</span></a></li>
                    </ul>

                    <h4 class="color-text-tertiary text-normal text-mono f5 mb-2 border-lg-top pt-lg-3">Connect with others</h4>
                    <ul class="list-style-none mb-0">
                      <li class="edge-item-fix"><a href="https://github.com/readme" class="py-2 lh-condensed-ultra d-block Link--secondary no-underline f5 Bump-link--hover">The ReadME Project <span class="Bump-link-symbol float-right text-normal color-text-tertiary pr-3">→</span></a></li>
                      <li class="edge-item-fix"><a href="https://github.com/events" class="py-2 lh-condensed-ultra d-block Link--secondary no-underline f5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Events">Events <span class="Bump-link-symbol float-right text-normal color-text-tertiary pr-3">→</span></a></li>
                      <li class="edge-item-fix"><a href="https://github.community/" class="py-2 lh-condensed-ultra d-block Link--secondary no-underline f5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Community forum">Community forum <span class="Bump-link-symbol float-right text-normal color-text-tertiary pr-3">→</span></a></li>
                      <li class="edge-item-fix"><a href="https://education.github.com/" class="py-2 lh-condensed-ultra d-block Link--secondary no-underline f5 Bump-link--hover" data-ga-click="(Logged out) Header, go to GitHub Education">GitHub Education <span class="Bump-link-symbol float-right text-normal color-text-tertiary pr-3">→</span></a></li>
                      <li class="edge-item-fix"><a href="https://stars.github.com/" class="py-2 pb-0 lh-condensed-ultra d-block Link--secondary no-underline f5 Bump-link--hover" data-ga-click="(Logged out) Header, go to GitHub Stars Program">GitHub Stars program <span class="Bump-link-symbol float-right text-normal color-text-tertiary pr-3">→</span></a></li>
                    </ul>
                  </div>
                </details>
              </li>

              <li class="border-bottom border-lg-bottom-0 mr-0 mr-lg-3">
                <a href="https://github.com/marketplace" class="HeaderMenu-link no-underline py-3 d-block d-lg-inline-block" data-ga-click="(Logged out) Header, go to Marketplace">Marketplace</a>
              </li>

              <li class="d-block d-lg-flex flex-lg-nowrap flex-lg-items-center border-bottom border-lg-bottom-0 mr-0 mr-lg-3 edge-item-fix position-relative flex-wrap flex-justify-between d-flex flex-items-center ">
                <details class="HeaderMenu-details details-overlay details-reset width-full">
                  <summary class="HeaderMenu-summary HeaderMenu-link px-0 py-3 border-0 no-wrap d-block d-lg-inline-block">
                    Pricing
                    <svg x="0px" y="0px" viewBox="0 0 14 8" xml:space="preserve" fill="none" class="icon-chevon-down-mktg position-absolute position-lg-relative" data-darkreader-inline-fill="" style="--darkreader-inline-fill:none;">
                       <path d="M1,1l6.2,6L13,1"></path>
                    </svg>
                  </summary>

                  <div class="dropdown-menu flex-auto rounded px-0 pt-2 pb-4 mt-0 p-lg-4 position-relative position-lg-absolute left-0 left-lg-n4">
                    <a href="https://github.com/pricing" class="pb-2 lh-condensed-ultra d-block Link--primary no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Pricing">Plans <span class="Bump-link-symbol float-right text-normal color-text-tertiary pr-3">→</span></a>

                    <ul class="list-style-none mb-3">
                      <li class="edge-item-fix"><a href="https://github.com/pricing#feature-comparison" class="py-2 lh-condensed-ultra d-block Link--secondary no-underline f5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Compare plans">Compare plans <span class="Bump-link-symbol float-right text-normal color-text-tertiary pr-3">→</span></a></li>
                      <li class="edge-item-fix"><a href="https://enterprise.github.com/contact" class="py-2 lh-condensed-ultra d-block Link--secondary no-underline f5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Contact Sales">Contact Sales <span class="Bump-link-symbol float-right text-normal color-text-tertiary pr-3">→</span></a></li>
                    </ul>

                    <ul class="list-style-none mb-0 border-lg-top pt-lg-3">
                      <li class="edge-item-fix"><a href="https://education.github.com/" class="py-2 pb-0 lh-condensed-ultra d-block no-underline Link--primary no-underline h5 Bump-link--hover" data-ga-click="(Logged out) Header, go to Education">Education <span class="Bump-link-symbol float-right text-normal color-text-tertiary pr-3">→</span></a></li>
                    </ul>
                  </div>
                </details>
              </li>
          </ul>
        </nav>

      <div class="d-lg-flex flex-items-center px-3 px-lg-0 text-center text-lg-left">
          <div class="d-lg-flex min-width-0 mb-3 mb-lg-0">
            


  <div class="header-search flex-auto js-site-search position-relative flex-self-stretch flex-md-self-auto mb-3 mb-md-0 mr-0 mr-md-3 scoped-search site-scoped-search js-jump-to">
    <div class="position-relative">
      <!-- '"` --><!-- </textarea></xmp> --><form class="js-site-search-form" role="search" aria-label="Site" data-scope-type="Repository" data-scope-id="107937815" data-scoped-search-url="/aws/amazon-sagemaker-examples/search" data-owner-scoped-search-url="/orgs/aws/search" data-unscoped-search-url="/search" action="https://github.com/aws/amazon-sagemaker-examples/search" accept-charset="UTF-8" method="get">
        <label class="form-control input-sm header-search-wrapper p-0 js-chromeless-input-container header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center">
          <input type="text" class="form-control input-sm header-search-input jump-to-field js-jump-to-field js-site-search-focus js-site-search-field is-clearable" data-hotkey="s,/" name="q" value="" placeholder="Search" data-unscoped-placeholder="Search GitHub" data-scoped-placeholder="Search" autocapitalize="off" role="combobox" aria-haspopup="listbox" aria-expanded="false" aria-autocomplete="list" aria-controls="jump-to-results" aria-label="Search" data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations" spellcheck="false" autocomplete="off">
          <input type="hidden" data-csrf="true" class="js-data-jump-to-suggestions-path-csrf" value="KeWLOqmlOwGUkCPHACfQoT/Y/FyETOcexv3nPPm5D2GZtd4zgM0GGH/TRAo3W5GnX4hHF/ONPdMlssDtkFxWEw==">
          <input type="hidden" class="js-site-search-type-field" name="type">
              <img src="./sklearn_abalone_featurizer_files/search-key-slash.svg" alt="" class="mr-2 header-search-key-slash">

            <div class="Box position-absolute overflow-hidden d-none jump-to-suggestions js-jump-to-suggestions-container">
              
<ul class="d-none js-jump-to-suggestions-template-container">
  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-suggestion" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="https://github.com/aws/amazon-sagemaker-examples/blob/master/sagemaker-python-sdk/scikit_learn_inference_pipeline/sklearn_abalone_featurizer.py" data-item-type="suggestion">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8zM5 12.25v3.25a.25.25 0 00.4.2l1.45-1.087a.25.25 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z"></path></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M1.75 0A1.75 1.75 0 000 1.75v12.5C0 15.216.784 16 1.75 16h12.5A1.75 1.75 0 0016 14.25V1.75A1.75 1.75 0 0014.25 0H1.75zM1.5 1.75a.25.25 0 01.25-.25h12.5a.25.25 0 01.25.25v12.5a.25.25 0 01-.25.25H1.75a.25.25 0 01-.25-.25V1.75zM11.75 3a.75.75 0 00-.75.75v7.5a.75.75 0 001.5 0v-7.5a.75.75 0 00-.75-.75zm-8.25.75a.75.75 0 011.5 0v5.5a.75.75 0 01-1.5 0v-5.5zM8 3a.75.75 0 00-.75.75v3.5a.75.75 0 001.5 0v-3.5A.75.75 0 008 3z"></path></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M11.5 7a4.499 4.499 0 11-8.998 0A4.499 4.499 0 0111.5 7zm-.82 4.74a6 6 0 111.06-1.06l3.04 3.04a.75.75 0 11-1.06 1.06l-3.04-3.04z"></path></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="https://github.com/aws/amazon-sagemaker-examples/blob/master/sagemaker-python-sdk/scikit_learn_inference_pipeline/sklearn_abalone_featurizer.py" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 color-bg-tertiary px-1 color-text-tertiary ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 color-bg-tertiary px-1 color-text-tertiary ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>

</ul>

<ul class="d-none js-jump-to-no-results-template-container">
  <li class="d-flex flex-justify-center flex-items-center f5 d-none js-jump-to-suggestion p-2">
    <span class="color-text-secondary">No suggested jump to results</span>
  </li>
</ul>

<ul id="jump-to-results" role="listbox" class="p-0 m-0 js-navigation-container jump-to-suggestions-results-container js-jump-to-suggestions-results-container">
  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-scoped-search d-none" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="https://github.com/aws/amazon-sagemaker-examples/blob/master/sagemaker-python-sdk/scikit_learn_inference_pipeline/sklearn_abalone_featurizer.py" data-item-type="scoped_search">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8zM5 12.25v3.25a.25.25 0 00.4.2l1.45-1.087a.25.25 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z"></path></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M1.75 0A1.75 1.75 0 000 1.75v12.5C0 15.216.784 16 1.75 16h12.5A1.75 1.75 0 0016 14.25V1.75A1.75 1.75 0 0014.25 0H1.75zM1.5 1.75a.25.25 0 01.25-.25h12.5a.25.25 0 01.25.25v12.5a.25.25 0 01-.25.25H1.75a.25.25 0 01-.25-.25V1.75zM11.75 3a.75.75 0 00-.75.75v7.5a.75.75 0 001.5 0v-7.5a.75.75 0 00-.75-.75zm-8.25.75a.75.75 0 011.5 0v5.5a.75.75 0 01-1.5 0v-5.5zM8 3a.75.75 0 00-.75.75v3.5a.75.75 0 001.5 0v-3.5A.75.75 0 008 3z"></path></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M11.5 7a4.499 4.499 0 11-8.998 0A4.499 4.499 0 0111.5 7zm-.82 4.74a6 6 0 111.06-1.06l3.04 3.04a.75.75 0 11-1.06 1.06l-3.04-3.04z"></path></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="https://github.com/aws/amazon-sagemaker-examples/blob/master/sagemaker-python-sdk/scikit_learn_inference_pipeline/sklearn_abalone_featurizer.py" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 color-bg-tertiary px-1 color-text-tertiary ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 color-bg-tertiary px-1 color-text-tertiary ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>

  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-owner-scoped-search d-none" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="https://github.com/aws/amazon-sagemaker-examples/blob/master/sagemaker-python-sdk/scikit_learn_inference_pipeline/sklearn_abalone_featurizer.py" data-item-type="owner_scoped_search">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8zM5 12.25v3.25a.25.25 0 00.4.2l1.45-1.087a.25.25 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z"></path></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M1.75 0A1.75 1.75 0 000 1.75v12.5C0 15.216.784 16 1.75 16h12.5A1.75 1.75 0 0016 14.25V1.75A1.75 1.75 0 0014.25 0H1.75zM1.5 1.75a.25.25 0 01.25-.25h12.5a.25.25 0 01.25.25v12.5a.25.25 0 01-.25.25H1.75a.25.25 0 01-.25-.25V1.75zM11.75 3a.75.75 0 00-.75.75v7.5a.75.75 0 001.5 0v-7.5a.75.75 0 00-.75-.75zm-8.25.75a.75.75 0 011.5 0v5.5a.75.75 0 01-1.5 0v-5.5zM8 3a.75.75 0 00-.75.75v3.5a.75.75 0 001.5 0v-3.5A.75.75 0 008 3z"></path></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M11.5 7a4.499 4.499 0 11-8.998 0A4.499 4.499 0 0111.5 7zm-.82 4.74a6 6 0 111.06-1.06l3.04 3.04a.75.75 0 11-1.06 1.06l-3.04-3.04z"></path></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="https://github.com/aws/amazon-sagemaker-examples/blob/master/sagemaker-python-sdk/scikit_learn_inference_pipeline/sklearn_abalone_featurizer.py" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 color-bg-tertiary px-1 color-text-tertiary ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this organization">
        In this organization
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 color-bg-tertiary px-1 color-text-tertiary ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>

  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-global-search d-none" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="https://github.com/aws/amazon-sagemaker-examples/blob/master/sagemaker-python-sdk/scikit_learn_inference_pipeline/sklearn_abalone_featurizer.py" data-item-type="global_search">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8zM5 12.25v3.25a.25.25 0 00.4.2l1.45-1.087a.25.25 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z"></path></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M1.75 0A1.75 1.75 0 000 1.75v12.5C0 15.216.784 16 1.75 16h12.5A1.75 1.75 0 0016 14.25V1.75A1.75 1.75 0 0014.25 0H1.75zM1.5 1.75a.25.25 0 01.25-.25h12.5a.25.25 0 01.25.25v12.5a.25.25 0 01-.25.25H1.75a.25.25 0 01-.25-.25V1.75zM11.75 3a.75.75 0 00-.75.75v7.5a.75.75 0 001.5 0v-7.5a.75.75 0 00-.75-.75zm-8.25.75a.75.75 0 011.5 0v5.5a.75.75 0 01-1.5 0v-5.5zM8 3a.75.75 0 00-.75.75v3.5a.75.75 0 001.5 0v-3.5A.75.75 0 008 3z"></path></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M11.5 7a4.499 4.499 0 11-8.998 0A4.499 4.499 0 0111.5 7zm-.82 4.74a6 6 0 111.06-1.06l3.04 3.04a.75.75 0 11-1.06 1.06l-3.04-3.04z"></path></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="https://github.com/aws/amazon-sagemaker-examples/blob/master/sagemaker-python-sdk/scikit_learn_inference_pipeline/sklearn_abalone_featurizer.py" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 color-bg-tertiary px-1 color-text-tertiary ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 color-bg-tertiary px-1 color-text-tertiary ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>


</ul>

            </div>
        </label>
</form>    </div>
  </div>

          </div>

        <div class="position-relative mr-3">
          <a href="https://github.com/login?return_to=%2Faws%2Famazon-sagemaker-examples%2Ftree%2Fmaster%2Fsagemaker-python-sdk%2Fscikit_learn_inference_pipeline" class="HeaderMenu-link flex-shrink-0 no-underline" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;site header menu&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;SIGN_UP&quot;,&quot;originating_url&quot;:&quot;https://github.com/aws/amazon-sagemaker-examples/tree/master/sagemaker-python-sdk/scikit_learn_inference_pipeline&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="25082527d5583c8328b5666127b38c51e703c690a1dfb94342999671a136d6e6" data-ga-click="(Logged out) Header, clicked Sign in, text:sign-in">
            Sign in
          </a>
        </div>

            <a href="https://github.com/signup?ref_cta=Sign+up&amp;ref_loc=header+logged+out&amp;ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E%2Ffiles%2Fdisambiguate&amp;source=header-repo&amp;source_repo=aws%2Famazon-sagemaker-examples" class="HeaderMenu-link flex-shrink-0 d-inline-block no-underline border color-border-tertiary rounded px-2 py-1" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;site header menu&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;SIGN_UP&quot;,&quot;originating_url&quot;:&quot;https://github.com/aws/amazon-sagemaker-examples/tree/master/sagemaker-python-sdk/scikit_learn_inference_pipeline&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="25082527d5583c8328b5666127b38c51e703c690a1dfb94342999671a136d6e6">
              Sign up
            </a>
      </div>
    </div>
  </div>
</header>

    </div>

  <div id="start-of-content" class="show-on-focus"></div>





    <div data-pjax-replace="" id="js-flash-container">


  <template class="js-flash-template"></template>
</div>


    

  <include-fragment class="js-notification-shelf-include-fragment" data-base-src="https://github.com/notifications/beta/shelf"></include-fragment>




  <div class="application-main " data-commit-hovercards-enabled="" data-discussion-hovercards-enabled="" data-issue-and-pr-hovercards-enabled="">
        <div itemscope="" itemtype="http://schema.org/SoftwareSourceCode" class="">
    <main id="js-repo-pjax-container" data-pjax-container="">
      
      
    






  


  <div class="hx_page-header-bg pt-3 hide-full-screen mb-5">

      <div class="d-flex mb-3 px-3 px-md-4 px-lg-5">

        <div class="flex-auto min-width-0 width-fit mr-3">
            <h1 class=" d-flex flex-wrap flex-items-center break-word f3 text-normal">
    <svg class="octicon octicon-repo color-text-secondary mr-2" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8zM5 12.25v3.25a.25.25 0 00.4.2l1.45-1.087a.25.25 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z"></path></svg>
  <span class="author flex-self-stretch" itemprop="author">
    <a class="url fn" rel="author" data-hovercard-type="organization" data-hovercard-url="/orgs/aws/hovercard" href="https://github.com/aws">aws</a>
  </span>
  <span class="mx-1 flex-self-stretch color-text-secondary">/</span>
  <strong itemprop="name" class="mr-2 flex-self-stretch">
    <a data-pjax="#js-repo-pjax-container" href="https://github.com/aws/amazon-sagemaker-examples">amazon-sagemaker-examples</a>
  </strong>
  
</h1>


        </div>

          <ul class="pagehead-actions flex-shrink-0 d-none d-md-inline" style="padding: 2px 0;">

  <li>
      <a class="tooltipped tooltipped-s btn btn-sm" aria-label="You must be signed in to change notification settings" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;notification subscription menu watch&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;LOG_IN&quot;,&quot;originating_url&quot;:&quot;https://github.com/aws/amazon-sagemaker-examples/tree/master/sagemaker-python-sdk/scikit_learn_inference_pipeline&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="572089b6b6a91c26c53fd1074fdc23ae4ce960ebc119aa711065f03313c94de0" href="https://github.com/login?return_to=%2Faws%2Famazon-sagemaker-examples">
    <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-bell">
    <path d="M8 16a2 2 0 001.985-1.75c.017-.137-.097-.25-.235-.25h-3.5c-.138 0-.252.113-.235.25A2 2 0 008 16z"></path><path fill-rule="evenodd" d="M8 1.5A3.5 3.5 0 004.5 5v2.947c0 .346-.102.683-.294.97l-1.703 2.556a.018.018 0 00-.003.01l.001.006c0 .002.002.004.004.006a.017.017 0 00.006.004l.007.001h10.964l.007-.001a.016.016 0 00.006-.004.016.016 0 00.004-.006l.001-.007a.017.017 0 00-.003-.01l-1.703-2.554a1.75 1.75 0 01-.294-.97V5A3.5 3.5 0 008 1.5zM3 5a5 5 0 0110 0v2.947c0 .05.015.098.042.139l1.703 2.555A1.518 1.518 0 0113.482 13H2.518a1.518 1.518 0 01-1.263-2.36l1.703-2.554A.25.25 0 003 7.947V5z"></path>
</svg>
    Notifications
</a>
  </li>

  <li>
          <a class="btn btn-sm btn-with-count  tooltipped tooltipped-s" aria-label="You must be signed in to star a repository" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;star button&quot;,&quot;repository_id&quot;:107937815,&quot;auth_type&quot;:&quot;LOG_IN&quot;,&quot;originating_url&quot;:&quot;https://github.com/aws/amazon-sagemaker-examples/tree/master/sagemaker-python-sdk/scikit_learn_inference_pipeline&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="677fbd48fa15ff515d2982b819c7f5ec0244ba62980529b180337a1cff999c96" href="https://github.com/login?return_to=%2Faws%2Famazon-sagemaker-examples">
      <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-star v-align-text-bottom mr-1">
    <path fill-rule="evenodd" d="M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.818 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25zm0 2.445L6.615 5.5a.75.75 0 01-.564.41l-3.097.45 2.24 2.184a.75.75 0 01.216.664l-.528 3.084 2.769-1.456a.75.75 0 01.698 0l2.77 1.456-.53-3.084a.75.75 0 01.216-.664l2.24-2.183-3.096-.45a.75.75 0 01-.564-.41L8 2.694v.001z"></path>
</svg>
      <span data-view-component="true">
        Star
</span></a>
    <a class="social-count js-social-count" href="https://github.com/aws/amazon-sagemaker-examples/stargazers" aria-label="5721 users starred this repository">
      5.7k
    </a>

  </li>

  <li>
        <a class="btn btn-sm btn-with-count tooltipped tooltipped-s" aria-label="You must be signed in to fork a repository" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;repo details fork button&quot;,&quot;repository_id&quot;:107937815,&quot;auth_type&quot;:&quot;LOG_IN&quot;,&quot;originating_url&quot;:&quot;https://github.com/aws/amazon-sagemaker-examples/tree/master/sagemaker-python-sdk/scikit_learn_inference_pipeline&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="2c265dce0a498e2985fea05064436b40161f713ae6a41de12d28fa125d54ca97" href="https://github.com/login?return_to=%2Faws%2Famazon-sagemaker-examples">
          <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-repo-forked">
    <path fill-rule="evenodd" d="M5 3.25a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm0 2.122a2.25 2.25 0 10-1.5 0v.878A2.25 2.25 0 005.75 8.5h1.5v2.128a2.251 2.251 0 101.5 0V8.5h1.5a2.25 2.25 0 002.25-2.25v-.878a2.25 2.25 0 10-1.5 0v.878a.75.75 0 01-.75.75h-4.5A.75.75 0 015 6.25v-.878zm3.75 7.378a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm3-8.75a.75.75 0 100-1.5.75.75 0 000 1.5z"></path>
</svg>
          Fork
</a>
      <a href="https://github.com/aws/amazon-sagemaker-examples/network/members" class="social-count" aria-label="4250 users forked this repository">
        4.3k
      </a>
  </li>
</ul>

      </div>
        

  <nav data-pjax="#js-repo-pjax-container" aria-label="Repository" data-view-component="true" class="js-repo-nav js-sidenav-container-pjax js-responsive-underlinenav overflow-hidden UnderlineNav px-3 px-md-4 px-lg-5">

    <ul data-view-component="true" class="UnderlineNav-body list-style-none">
        <li data-view-component="true" class="d-flex">
  <a href="https://github.com/aws/amazon-sagemaker-examples" data-tab-item="i0code-tab" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages repo_deployments /aws/amazon-sagemaker-examples" data-hotkey="g c" data-ga-click="Repository, Navigation click, Code tab" aria-current="page" data-view-component="true" class="UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item selected">
    
                  <svg class="octicon octicon-code UnderlineNav-octicon d-none d-sm-inline" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4.72 3.22a.75.75 0 011.06 1.06L2.06 8l3.72 3.72a.75.75 0 11-1.06 1.06L.47 8.53a.75.75 0 010-1.06l4.25-4.25zm6.56 0a.75.75 0 10-1.06 1.06L13.94 8l-3.72 3.72a.75.75 0 101.06 1.06l4.25-4.25a.75.75 0 000-1.06l-4.25-4.25z"></path></svg>
          <span data-content="Code">Code</span>
            <span title="Not available" data-view-component="true" class="Counter"></span>

    
</a></li>
        <li data-view-component="true" class="d-flex">
  <a href="https://github.com/aws/amazon-sagemaker-examples/issues" data-tab-item="i1issues-tab" data-selected-links="repo_issues repo_labels repo_milestones /aws/amazon-sagemaker-examples/issues" data-hotkey="g i" data-ga-click="Repository, Navigation click, Issues tab" data-view-component="true" class="UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
                  <svg class="octicon octicon-issue-opened UnderlineNav-octicon d-none d-sm-inline" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="M8 9.5a1.5 1.5 0 100-3 1.5 1.5 0 000 3z"></path><path fill-rule="evenodd" d="M8 0a8 8 0 100 16A8 8 0 008 0zM1.5 8a6.5 6.5 0 1113 0 6.5 6.5 0 01-13 0z"></path></svg>
          <span data-content="Issues">Issues</span>
            <span title="509" data-view-component="true" class="Counter">509</span>

    
</a></li>
        <li data-view-component="true" class="d-flex">
  <a href="https://github.com/aws/amazon-sagemaker-examples/pulls" data-tab-item="i2pull-requests-tab" data-selected-links="repo_pulls checks /aws/amazon-sagemaker-examples/pulls" data-hotkey="g p" data-ga-click="Repository, Navigation click, Pull requests tab" data-view-component="true" class="UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
                  <svg class="octicon octicon-git-pull-request UnderlineNav-octicon d-none d-sm-inline" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.177 3.073L9.573.677A.25.25 0 0110 .854v4.792a.25.25 0 01-.427.177L7.177 3.427a.25.25 0 010-.354zM3.75 2.5a.75.75 0 100 1.5.75.75 0 000-1.5zm-2.25.75a2.25 2.25 0 113 2.122v5.256a2.251 2.251 0 11-1.5 0V5.372A2.25 2.25 0 011.5 3.25zM11 2.5h-1V4h1a1 1 0 011 1v5.628a2.251 2.251 0 101.5 0V5A2.5 2.5 0 0011 2.5zm1 10.25a.75.75 0 111.5 0 .75.75 0 01-1.5 0zM3.75 12a.75.75 0 100 1.5.75.75 0 000-1.5z"></path></svg>
          <span data-content="Pull requests">Pull requests</span>
            <span title="101" data-view-component="true" class="Counter">101</span>

    
</a></li>
        <li data-view-component="true" class="d-flex">
  <a href="https://github.com/aws/amazon-sagemaker-examples/discussions" data-tab-item="i3discussions-tab" data-selected-links="repo_discussions /aws/amazon-sagemaker-examples/discussions" data-hotkey="g g" data-ga-click="Repository, Navigation click, Discussions tab" data-pjax="#repo-content-pjax-container" data-view-component="true" class="UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
                  <svg class="octicon octicon-comment-discussion UnderlineNav-octicon d-none d-sm-inline" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M1.5 2.75a.25.25 0 01.25-.25h8.5a.25.25 0 01.25.25v5.5a.25.25 0 01-.25.25h-3.5a.75.75 0 00-.53.22L3.5 11.44V9.25a.75.75 0 00-.75-.75h-1a.25.25 0 01-.25-.25v-5.5zM1.75 1A1.75 1.75 0 000 2.75v5.5C0 9.216.784 10 1.75 10H2v1.543a1.457 1.457 0 002.487 1.03L7.061 10h3.189A1.75 1.75 0 0012 8.25v-5.5A1.75 1.75 0 0010.25 1h-8.5zM14.5 4.75a.25.25 0 00-.25-.25h-.5a.75.75 0 110-1.5h.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0114.25 12H14v1.543a1.457 1.457 0 01-2.487 1.03L9.22 12.28a.75.75 0 111.06-1.06l2.22 2.22v-2.19a.75.75 0 01.75-.75h1a.25.25 0 00.25-.25v-5.5z"></path></svg>
          <span data-content="Discussions">Discussions</span>
            <span title="Not available" data-view-component="true" class="Counter"></span>

    
</a></li>
        <li data-view-component="true" class="d-flex">
  <a href="https://github.com/aws/amazon-sagemaker-examples/actions" data-tab-item="i4actions-tab" data-selected-links="repo_actions /aws/amazon-sagemaker-examples/actions" data-hotkey="g a" data-ga-click="Repository, Navigation click, Actions tab" data-view-component="true" class="UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
                  <svg class="octicon octicon-play UnderlineNav-octicon d-none d-sm-inline" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M1.5 8a6.5 6.5 0 1113 0 6.5 6.5 0 01-13 0zM8 0a8 8 0 100 16A8 8 0 008 0zM6.379 5.227A.25.25 0 006 5.442v5.117a.25.25 0 00.379.214l4.264-2.559a.25.25 0 000-.428L6.379 5.227z"></path></svg>
          <span data-content="Actions">Actions</span>
            <span title="Not available" data-view-component="true" class="Counter"></span>

    
</a></li>
        <li data-view-component="true" class="d-flex">
  <a href="https://github.com/aws/amazon-sagemaker-examples/projects" data-tab-item="i5projects-tab" data-selected-links="repo_projects new_repo_project repo_project /aws/amazon-sagemaker-examples/projects" data-hotkey="g b" data-ga-click="Repository, Navigation click, Projects tab" data-view-component="true" class="UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
                  <svg class="octicon octicon-project UnderlineNav-octicon d-none d-sm-inline" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M1.75 0A1.75 1.75 0 000 1.75v12.5C0 15.216.784 16 1.75 16h12.5A1.75 1.75 0 0016 14.25V1.75A1.75 1.75 0 0014.25 0H1.75zM1.5 1.75a.25.25 0 01.25-.25h12.5a.25.25 0 01.25.25v12.5a.25.25 0 01-.25.25H1.75a.25.25 0 01-.25-.25V1.75zM11.75 3a.75.75 0 00-.75.75v7.5a.75.75 0 001.5 0v-7.5a.75.75 0 00-.75-.75zm-8.25.75a.75.75 0 011.5 0v5.5a.75.75 0 01-1.5 0v-5.5zM8 3a.75.75 0 00-.75.75v3.5a.75.75 0 001.5 0v-3.5A.75.75 0 008 3z"></path></svg>
          <span data-content="Projects">Projects</span>
            <span title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>

    
</a></li>
        <li data-view-component="true" class="d-flex">
  <a href="https://github.com/aws/amazon-sagemaker-examples/security" data-tab-item="i6security-tab" data-selected-links="security overview alerts policy token_scanning code_scanning /aws/amazon-sagemaker-examples/security" data-hotkey="g s" data-ga-click="Repository, Navigation click, Security tab" data-view-component="true" class="UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
                  <svg class="octicon octicon-shield UnderlineNav-octicon d-none d-sm-inline" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.467.133a1.75 1.75 0 011.066 0l5.25 1.68A1.75 1.75 0 0115 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.7 1.7 0 01-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 011.217-1.667l5.25-1.68zm.61 1.429a.25.25 0 00-.153 0l-5.25 1.68a.25.25 0 00-.174.238V7c0 1.358.275 2.666 1.057 3.86.784 1.194 2.121 2.34 4.366 3.297a.2.2 0 00.154 0c2.245-.956 3.582-2.104 4.366-3.298C13.225 9.666 13.5 8.36 13.5 7V3.48a.25.25 0 00-.174-.237l-5.25-1.68zM9 10.5a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.75a.75.75 0 10-1.5 0v3a.75.75 0 001.5 0v-3z"></path></svg>
          <span data-content="Security">Security</span>
            

    
</a></li>
        <li data-view-component="true" class="d-flex">
  <a href="https://github.com/aws/amazon-sagemaker-examples/pulse" data-tab-item="i7insights-tab" data-selected-links="repo_graphs repo_contributors dependency_graph dependabot_updates pulse people community /aws/amazon-sagemaker-examples/pulse" data-ga-click="Repository, Navigation click, Insights tab" data-view-component="true" class="UnderlineNav-item hx_underlinenav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
                  <svg class="octicon octicon-graph UnderlineNav-octicon d-none d-sm-inline" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M1.5 1.75a.75.75 0 00-1.5 0v12.5c0 .414.336.75.75.75h14.5a.75.75 0 000-1.5H1.5V1.75zm14.28 2.53a.75.75 0 00-1.06-1.06L10 7.94 7.53 5.47a.75.75 0 00-1.06 0L3.22 8.72a.75.75 0 001.06 1.06L7 7.06l2.47 2.47a.75.75 0 001.06 0l5.25-5.25z"></path></svg>
          <span data-content="Insights">Insights</span>
            <span title="Not available" data-view-component="true" class="Counter"></span>

    
</a></li>
</ul>
      <div style="visibility:hidden;" data-view-component="true" class="UnderlineNav-actions  js-responsive-underlinenav-overflow position-absolute pr-3 pr-md-4 pr-lg-5 right-0">      <details data-view-component="true" class="details-overlay details-reset position-relative">
  <summary role="button" data-view-component="true">          <div class="UnderlineNav-item mr-0 border-0">
            <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-kebab-horizontal">
    <path d="M8 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zM1.5 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zm13 0a1.5 1.5 0 100-3 1.5 1.5 0 000 3z"></path>
</svg>
            <span class="sr-only">More</span>
          </div>
</summary>
  <div data-view-component="true">          <details-menu role="menu" data-view-component="true" class="dropdown-menu dropdown-menu-sw">
  
            <ul>
                <li data-menu-item="i0code-tab" hidden="">
                  <a role="menuitem" class="js-selected-navigation-item selected dropdown-item" aria-current="page" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages repo_deployments /aws/amazon-sagemaker-examples" href="https://github.com/aws/amazon-sagemaker-examples">
                    Code
</a>                </li>
                <li data-menu-item="i1issues-tab" hidden="">
                  <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="repo_issues repo_labels repo_milestones /aws/amazon-sagemaker-examples/issues" href="https://github.com/aws/amazon-sagemaker-examples/issues">
                    Issues
</a>                </li>
                <li data-menu-item="i2pull-requests-tab" hidden="">
                  <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="repo_pulls checks /aws/amazon-sagemaker-examples/pulls" href="https://github.com/aws/amazon-sagemaker-examples/pulls">
                    Pull requests
</a>                </li>
                <li data-menu-item="i3discussions-tab" hidden="">
                  <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="repo_discussions /aws/amazon-sagemaker-examples/discussions" href="https://github.com/aws/amazon-sagemaker-examples/discussions">
                    Discussions
</a>                </li>
                <li data-menu-item="i4actions-tab" hidden="">
                  <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="repo_actions /aws/amazon-sagemaker-examples/actions" href="https://github.com/aws/amazon-sagemaker-examples/actions">
                    Actions
</a>                </li>
                <li data-menu-item="i5projects-tab" hidden="">
                  <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="repo_projects new_repo_project repo_project /aws/amazon-sagemaker-examples/projects" href="https://github.com/aws/amazon-sagemaker-examples/projects">
                    Projects
</a>                </li>
                <li data-menu-item="i6security-tab" hidden="">
                  <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="security overview alerts policy token_scanning code_scanning /aws/amazon-sagemaker-examples/security" href="https://github.com/aws/amazon-sagemaker-examples/security">
                    Security
</a>                </li>
                <li data-menu-item="i7insights-tab" hidden="">
                  <a role="menuitem" class="js-selected-navigation-item dropdown-item" data-selected-links="repo_graphs repo_contributors dependency_graph dependabot_updates pulse people community /aws/amazon-sagemaker-examples/pulse" href="https://github.com/aws/amazon-sagemaker-examples/pulse">
                    Insights
</a>                </li>
            </ul>

</details-menu></div>
</details></div>
</nav>

  </div>


<div class="container-xl clearfix new-discussion-timeline px-3 px-md-4 px-lg-5">
  <div id="repo-content-pjax-container" class="repository-content ">


  
<div>
  


    <a class="d-none js-permalink-shortcut" data-hotkey="y" href="https://github.com/aws/amazon-sagemaker-examples/blob/2e95ceb9f5f6128863d976c9174ecbe2822e444a/sagemaker-python-sdk/scikit_learn_inference_pipeline/sklearn_abalone_featurizer.py">Permalink</a>

    <!-- blob contrib key: blob_contributors:v22:5b82142d581b34bfb39c143f25e7d406172fbfe12967e73063ae009400fe5b91 -->

    <div class="d-flex flex-items-start flex-shrink-0 pb-3 flex-wrap flex-md-nowrap flex-justify-between flex-md-justify-start">
      
<div class="position-relative">
  <details class="details-reset details-overlay mr-0 mb-0 " id="branch-select-menu">
    <summary class="btn css-truncate" data-hotkey="w" title="Switch branches or tags">
      <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-git-branch text-gray">
    <path fill-rule="evenodd" d="M11.75 2.5a.75.75 0 100 1.5.75.75 0 000-1.5zm-2.25.75a2.25 2.25 0 113 2.122V6A2.5 2.5 0 0110 8.5H6a1 1 0 00-1 1v1.128a2.251 2.251 0 11-1.5 0V5.372a2.25 2.25 0 111.5 0v1.836A2.492 2.492 0 016 7h4a1 1 0 001-1v-.628A2.25 2.25 0 019.5 3.25zM4.25 12a.75.75 0 100 1.5.75.75 0 000-1.5zM3.5 3.25a.75.75 0 111.5 0 .75.75 0 01-1.5 0z"></path>
</svg>
      <span class="css-truncate-target" data-menu-button="">master</span>
      <span class="dropdown-caret"></span>
    </summary>

      
<div class="SelectMenu">
  <div class="SelectMenu-modal">
    <header class="SelectMenu-header">
      <span class="SelectMenu-title">Switch branches/tags</span>
      <button class="SelectMenu-closeButton" type="button" data-toggle-for="branch-select-menu"><svg aria-label="Close menu" aria-hidden="false" role="img" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-x">
    <path fill-rule="evenodd" d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z"></path>
</svg></button>
    </header>

    <input-demux data-action="tab-container-change:input-demux#storeInput tab-container-changed:input-demux#updateInput" data-catalyst="">
      <tab-container class="d-flex flex-column js-branches-tags-tabs" style="min-height: 0;">
        <div class="SelectMenu-filter">
          <input data-target="input-demux.source" id="context-commitish-filter-field" class="SelectMenu-input form-control" aria-owns="ref-list-branches" data-controls-ref-menu-id="ref-list-branches" autofocus="" autocomplete="off" aria-label="Filter branches/tags" placeholder="Filter branches/tags" type="text">
        </div>

        <div class="SelectMenu-tabs" role="tablist" data-target="input-demux.control">
          <button class="SelectMenu-tab" type="button" role="tab" aria-selected="true" tabindex="0">Branches</button>
          <button class="SelectMenu-tab" type="button" role="tab" aria-selected="false" tabindex="-1">Tags</button>
        </div>

        <div role="tabpanel" id="ref-list-branches" data-filter-placeholder="Filter branches/tags" class="d-flex flex-column flex-auto overflow-auto" tabindex="">
          <ref-selector type="branch" data-targets="input-demux.sinks" data-action="
              input-entered:ref-selector#inputEntered
              tab-selected:ref-selector#tabSelected
              focus-list:ref-selector#focusFirstListMember
            " query-endpoint="/aws/amazon-sagemaker-examples/refs" cache-key="v0:1625693884.491698" current-committish="bWFzdGVy" default-branch="bWFzdGVy" name-with-owner="YXdzL2FtYXpvbi1zYWdlbWFrZXItZXhhbXBsZXM=" data-catalyst="">

            <template data-target="ref-selector.fetchFailedTemplate"></template>

              <template data-target="ref-selector.noMatchTemplate"></template>


            <!-- TODO: this max-height is necessary or else the branch list won't scroll.  why? -->
            <div data-target="ref-selector.listContainer" role="menu" class="SelectMenu-list " style="max-height: 330px" data-pjax="#repo-content-pjax-container">
              <div class="SelectMenu-loading pt-3 pb-0" aria-label="Menu is loading">
                <svg style="box-sizing: content-box; color: var(--color-icon-primary); --darkreader-inline-fill:none; --darkreader-inline-color:var(--darkreader-text--color-icon-primary);" viewBox="0 0 16 16" fill="none" data-view-component="true" width="32" height="32" class="anim-rotate" data-darkreader-inline-fill="" data-darkreader-inline-color="">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" data-darkreader-inline-stroke="" style="--darkreader-inline-stroke:currentColor;"></circle>
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke" data-darkreader-inline-stroke="" style="--darkreader-inline-stroke:currentColor;"></path>
</svg>
              </div>
            </div>

              <template data-target="ref-selector.itemTemplate"></template>


              <footer class="SelectMenu-footer"><a href="https://github.com/aws/amazon-sagemaker-examples/branches">View all branches</a></footer>
          </ref-selector>

        </div>

        <div role="tabpanel" id="tags-menu" data-filter-placeholder="Find a tag" class="d-flex flex-column flex-auto overflow-auto" tabindex="" hidden="">
          <ref-selector type="tag" data-action="
              input-entered:ref-selector#inputEntered
              tab-selected:ref-selector#tabSelected
              focus-list:ref-selector#focusFirstListMember
            " data-targets="input-demux.sinks" query-endpoint="/aws/amazon-sagemaker-examples/refs" cache-key="v0:1625693884.491698" current-committish="bWFzdGVy" default-branch="bWFzdGVy" name-with-owner="YXdzL2FtYXpvbi1zYWdlbWFrZXItZXhhbXBsZXM=" data-catalyst="">

            <template data-target="ref-selector.fetchFailedTemplate"></template>

            <template data-target="ref-selector.noMatchTemplate"></template>

              <template data-target="ref-selector.itemTemplate"></template>


            <div data-target="ref-selector.listContainer" role="menu" class="SelectMenu-list" style="max-height: 330px" data-pjax="#repo-content-pjax-container">
              <div class="SelectMenu-loading pt-3 pb-0" aria-label="Menu is loading">
                <svg style="box-sizing: content-box; color: var(--color-icon-primary); --darkreader-inline-fill:none; --darkreader-inline-color:var(--darkreader-text--color-icon-primary);" viewBox="0 0 16 16" fill="none" data-view-component="true" width="32" height="32" class="anim-rotate" data-darkreader-inline-fill="" data-darkreader-inline-color="">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" data-darkreader-inline-stroke="" style="--darkreader-inline-stroke:currentColor;"></circle>
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke" data-darkreader-inline-stroke="" style="--darkreader-inline-stroke:currentColor;"></path>
</svg>
              </div>
            </div>
              <footer class="SelectMenu-footer"><a href="https://github.com/aws/amazon-sagemaker-examples/tags">View all tags</a></footer>
          </ref-selector>
        </div>
      </tab-container>
    </input-demux>
  </div>
</div>

  </details>

</div>

      <h2 id="blob-path" class="breadcrumb flex-auto flex-self-center min-width-0 text-normal mx-2 width-full width-md-auto flex-order-1 flex-md-order-none mt-3 mt-md-0">
        <span class="js-repo-root text-bold"><span class="js-path-segment d-inline-block wb-break-all"><a data-pjax="#repo-content-pjax-container" href="https://github.com/aws/amazon-sagemaker-examples"><span>amazon-sagemaker-examples</span></a></span></span><span class="separator">/</span><span class="js-path-segment d-inline-block wb-break-all"><a data-pjax="#repo-content-pjax-container" href="https://github.com/aws/amazon-sagemaker-examples/tree/master/sagemaker-python-sdk"><span>sagemaker-python-sdk</span></a></span><span class="separator">/</span><span class="js-path-segment d-inline-block wb-break-all"><a data-pjax="#repo-content-pjax-container" href="https://github.com/aws/amazon-sagemaker-examples/tree/master/sagemaker-python-sdk/scikit_learn_inference_pipeline"><span>scikit_learn_inference_pipeline</span></a></span><span class="separator">/</span><strong class="final-path">sklearn_abalone_featurizer.py</strong>
          <span class="separator">/</span><details class="details-reset details-overlay d-inline" id="jumpto-symbol-select-menu">
  <summary class="btn-link Link--secondary css-truncate" aria-haspopup="menu" data-hotkey="r" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.click_on_blob_definitions&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;click_on_blob_definitions&quot;,&quot;repository_id&quot;:107937815,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/aws/amazon-sagemaker-examples/blob/master/sagemaker-python-sdk/scikit_learn_inference_pipeline/sklearn_abalone_featurizer.py?_pjax=%23repo-content-pjax-container&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="9faf9a7e9c2b1c73157ba2637e10a53cb02a307af6ff4713aa80c21c8cd423a0" role="button">
      <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-code">
    <path fill-rule="evenodd" d="M4.72 3.22a.75.75 0 011.06 1.06L2.06 8l3.72 3.72a.75.75 0 11-1.06 1.06L.47 8.53a.75.75 0 010-1.06l4.25-4.25zm6.56 0a.75.75 0 10-1.06 1.06L13.94 8l-3.72 3.72a.75.75 0 101.06 1.06l4.25-4.25a.75.75 0 000-1.06l-4.25-4.25z"></path>
</svg>
    <span data-menu-button="">Jump to</span>
    <span class="dropdown-caret"></span>
  </summary>
  <details-menu class="SelectMenu SelectMenu--hasFilter" role="menu">
    <div class="SelectMenu-modal">
      <header class="SelectMenu-header">
        <span class="SelectMenu-title">Code definitions</span>
        <button class="SelectMenu-closeButton" type="button" data-toggle-for="jumpto-symbol-select-menu">
          <svg aria-label="Close menu" role="img" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-x">
    <path fill-rule="evenodd" d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z"></path>
</svg>
        </button>
      </header>
        <div class="SelectMenu-filter">
          <input class="SelectMenu-input form-control js-filterable-field" id="jumpto-symbols-filter-field" type="text" autocomplete="off" spellcheck="false" autofocus="" placeholder="Filter definitions" aria-label="Filter definitions">
        </div>
      <div class="SelectMenu-list">
        <div data-filterable-for="jumpto-symbols-filter-field" data-filterable-type="substring">
            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:107937815,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/aws/amazon-sagemaker-examples/blob/master/sagemaker-python-sdk/scikit_learn_inference_pipeline/sklearn_abalone_featurizer.py?_pjax=%23repo-content-pjax-container&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="ca8094a5404479f80a01a25bdffa44273724db516b5b9bcd175304e1c36939ef" href="https://github.com/aws/amazon-sagemaker-examples/blob/master/sagemaker-python-sdk/scikit_learn_inference_pipeline/sklearn_abalone_featurizer.py#L56">
              <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text="">merge_two_dicts</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:107937815,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/aws/amazon-sagemaker-examples/blob/master/sagemaker-python-sdk/scikit_learn_inference_pipeline/sklearn_abalone_featurizer.py?_pjax=%23repo-content-pjax-container&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="ca8094a5404479f80a01a25bdffa44273724db516b5b9bcd175304e1c36939ef" href="https://github.com/aws/amazon-sagemaker-examples/blob/master/sagemaker-python-sdk/scikit_learn_inference_pipeline/sklearn_abalone_featurizer.py#L135">
              <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text="">input_fn</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:107937815,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/aws/amazon-sagemaker-examples/blob/master/sagemaker-python-sdk/scikit_learn_inference_pipeline/sklearn_abalone_featurizer.py?_pjax=%23repo-content-pjax-container&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="ca8094a5404479f80a01a25bdffa44273724db516b5b9bcd175304e1c36939ef" href="https://github.com/aws/amazon-sagemaker-examples/blob/master/sagemaker-python-sdk/scikit_learn_inference_pipeline/sklearn_abalone_featurizer.py#L158">
              <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text="">output_fn</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:107937815,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/aws/amazon-sagemaker-examples/blob/master/sagemaker-python-sdk/scikit_learn_inference_pipeline/sklearn_abalone_featurizer.py?_pjax=%23repo-content-pjax-container&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="ca8094a5404479f80a01a25bdffa44273724db516b5b9bcd175304e1c36939ef" href="https://github.com/aws/amazon-sagemaker-examples/blob/master/sagemaker-python-sdk/scikit_learn_inference_pipeline/sklearn_abalone_featurizer.py#L179">
              <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text="">predict_fn</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>            <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:107937815,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/aws/amazon-sagemaker-examples/blob/master/sagemaker-python-sdk/scikit_learn_inference_pipeline/sklearn_abalone_featurizer.py?_pjax=%23repo-content-pjax-container&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="ca8094a5404479f80a01a25bdffa44273724db516b5b9bcd175304e1c36939ef" href="https://github.com/aws/amazon-sagemaker-examples/blob/master/sagemaker-python-sdk/scikit_learn_inference_pipeline/sklearn_abalone_featurizer.py#L199">
              <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check">
    <path fill-rule="evenodd" d="M13.78 4.22a.75.75 0 010 1.06l-7.25 7.25a.75.75 0 01-1.06 0L2.22 9.28a.75.75 0 011.06-1.06L6 10.94l6.72-6.72a.75.75 0 011.06 0z"></path>
</svg>
              <span class="flex-auto css-truncate-target" data-menu-button-text="">model_fn</span>
              <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>        </div>
      </div>
      <footer class="SelectMenu-footer">
        <div class="d-flex flex-justify-between">
          Code navigation index up-to-date
          <svg class="octicon octicon-dot-fill text-green" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8z"></path></svg>
        </div>
      </footer>
    </div>
  </details-menu>
</details>

      </h2>
      <a href="https://github.com/aws/amazon-sagemaker-examples/find/master" class="js-pjax-capture-input btn mr-2 d-none d-md-block" data-pjax="" data-hotkey="t">
        Go to file
      </a>

      <details id="blob-more-options-details" data-view-component="true" class="details-overlay details-reset position-relative">
  <summary role="button" data-view-component="true" class="btn">
  
            <svg aria-label="More options" role="img" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-kebab-horizontal">
    <path d="M8 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zM1.5 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zm13 0a1.5 1.5 0 100-3 1.5 1.5 0 000 3z"></path>
</svg>

  

</summary>
  <div data-view-component="true">          <ul class="dropdown-menu dropdown-menu-sw">
            <li class="d-block d-md-none">
              <a class="dropdown-item d-flex flex-items-baseline" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;FIND_FILE_BUTTON&quot;,&quot;repository_id&quot;:107937815,&quot;originating_url&quot;:&quot;https://github.com/aws/amazon-sagemaker-examples/blob/master/sagemaker-python-sdk/scikit_learn_inference_pipeline/sklearn_abalone_featurizer.py?_pjax=%23repo-content-pjax-container&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="49d3017d425eb41b55c1af6a29a2176b26c413805389b96e78a13efc403ac230" data-ga-click="Repository, find file, location:repo overview" data-hotkey="t" data-pjax="true" href="https://github.com/aws/amazon-sagemaker-examples/find/master">
                <span class="flex-auto">Go to file</span>
                <span class="text-small color-text-secondary" aria-hidden="true">T</span>
</a>            </li>
            <li data-toggle-for="blob-more-options-details">
              <button type="button" data-toggle-for="jumpto-line-details-dialog" class="btn-link dropdown-item">
                <span class="d-flex flex-items-baseline">
                  <span class="flex-auto">Go to line</span>
                  <span class="text-small color-text-secondary" aria-hidden="true">L</span>
                </span>
              </button>
            </li>
            <li data-toggle-for="blob-more-options-details">
              <button type="button" data-toggle-for="jumpto-symbol-select-menu" class="btn-link dropdown-item">
                <span class="d-flex flex-items-baseline">
                  <span class="flex-auto">Go to definition</span>
                  <span class="text-small color-text-secondary" aria-hidden="true">R</span>
                </span>
              </button>
            </li>
            <li class="dropdown-divider" role="none"></li>
            <li>
              <clipboard-copy value="sagemaker-python-sdk/scikit_learn_inference_pipeline/sklearn_abalone_featurizer.py" class="dropdown-item cursor-pointer" data-toggle-for="blob-more-options-details" tabindex="0" role="button">
                Copy path
              </clipboard-copy>
            </li>
            <li>
              <clipboard-copy value="https://github.com/aws/amazon-sagemaker-examples/blob/2e95ceb9f5f6128863d976c9174ecbe2822e444a/sagemaker-python-sdk/scikit_learn_inference_pipeline/sklearn_abalone_featurizer.py" class="dropdown-item cursor-pointer" data-toggle-for="blob-more-options-details" tabindex="0" role="button">
                <span class="d-flex flex-items-baseline">
                  <span class="flex-auto">Copy permalink</span>
                </span>
              </clipboard-copy>
            </li>
          </ul>
</div>
</details>    </div>




    <div class="Box d-flex flex-column flex-shrink-0 mb-3">
      

  <div class="Box-header Box-header--blue Details js-details-container">
      <div class="d-flex flex-items-center">
        <span class="flex-shrink-0 ml-n1 mr-n1 mt-n1 mb-n1">
          <a rel="contributor" data-skip-pjax="true" data-hovercard-type="user" data-hovercard-url="/users/ajaykarpur/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ajaykarpur"><img class="avatar avatar-user" src="./sklearn_abalone_featurizer_files/5490371" width="24" height="24" alt="@ajaykarpur"></a>
        </span>
        <div class="flex-1 d-flex flex-items-center ml-3 min-width-0">
          <div class="css-truncate css-truncate-overflow">
            <a class="text-bold Link--primary" rel="contributor" data-hovercard-type="user" data-hovercard-url="/users/ajaykarpur/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/ajaykarpur">ajaykarpur</a>

              <span class="markdown-title">
                <a data-pjax="true" title="infra: sort imports in all .py files with isort (#2225)" class="Link--secondary" href="https://github.com/aws/amazon-sagemaker-examples/commit/187e52fc3db844645b469cc35122ccbc188357a1">infra: sort imports in all .py files with isort (</a><a class="issue-link js-issue-link" data-error-text="Failed to load title" data-id="889017838" data-permission-text="Title is private" data-url="https://github.com/aws/amazon-sagemaker-examples/issues/2225" data-hovercard-type="pull_request" data-hovercard-url="/aws/amazon-sagemaker-examples/pull/2225/hovercard" href="https://github.com/aws/amazon-sagemaker-examples/pull/2225">#2225</a><a data-pjax="true" title="infra: sort imports in all .py files with isort (#2225)" class="Link--secondary" href="https://github.com/aws/amazon-sagemaker-examples/commit/187e52fc3db844645b469cc35122ccbc188357a1">)</a>
              </span>
          </div>


          <span class="ml-2">
            
  <details class="commit-build-statuses details-overlay details-reset js-dropdown-details hx_dropdown-fullscreen" data-deferred-details-content-url="/_render_node/MDE3OlN0YXR1c0NoZWNrUm9sbHVwMTA3OTM3ODE1OjE4N2U1MmZjM2RiODQ0NjQ1YjQ2OWNjMzUxMjJjY2JjMTg4MzU3YTE=/statuses/combined_branch_status">
    <summary class="color-text-danger">
      <svg aria-label="0 / 2 checks OK" class="octicon octicon-x" viewBox="0 0 16 16" version="1.1" width="16" height="16" role="img"><path fill-rule="evenodd" d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z"></path></svg>
    </summary>
    <div class="dropdown-menu dropdown-menu-e overflow-hidden">
      <include-fragment class="m-4 d-flex flex-column flex-items-center">
        <svg style="box-sizing: content-box; color: var(--color-icon-primary); --darkreader-inline-fill:none; --darkreader-inline-color:var(--darkreader-text--color-icon-primary);" viewBox="0 0 16 16" fill="none" data-view-component="true" width="32" height="32" class="anim-rotate" data-darkreader-inline-fill="" data-darkreader-inline-color="">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" data-darkreader-inline-stroke="" style="--darkreader-inline-stroke:currentColor;"></circle>
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke" data-darkreader-inline-stroke="" style="--darkreader-inline-stroke:currentColor;"></path>
</svg>
        <div class="color-text-secondary no-wrap">Loading status checks…</div>
      </include-fragment>
    </div>
  </details>

          </span>
        </div>
        <div class="ml-3 d-flex flex-shrink-0 flex-items-center flex-justify-end color-text-secondary no-wrap">
          <span class="d-none d-md-inline">
            <span>Latest commit</span>
            <a class="text-small text-mono Link--secondary" href="https://github.com/aws/amazon-sagemaker-examples/commit/187e52fc3db844645b469cc35122ccbc188357a1" data-pjax="">187e52f</a>
            <span itemprop="dateModified"><relative-time datetime="2021-05-11T23:00:33Z" class="no-wrap" title="May 12, 2021, 8:00 AM GMT+9">on May 12</relative-time></span>
          </span>

          <a data-pjax="" href="https://github.com/aws/amazon-sagemaker-examples/commits/master/sagemaker-python-sdk/scikit_learn_inference_pipeline/sklearn_abalone_featurizer.py" class="ml-3 no-wrap Link--primary no-underline">
            <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-history text-gray">
    <path fill-rule="evenodd" d="M1.643 3.143L.427 1.927A.25.25 0 000 2.104V5.75c0 .138.112.25.25.25h3.646a.25.25 0 00.177-.427L2.715 4.215a6.5 6.5 0 11-1.18 4.458.75.75 0 10-1.493.154 8.001 8.001 0 101.6-5.684zM7.75 4a.75.75 0 01.75.75v2.992l2.028.812a.75.75 0 01-.557 1.392l-2.5-1A.75.75 0 017 8.25v-3.5A.75.75 0 017.75 4z"></path>
</svg>
            <span class="d-none d-sm-inline">
              <strong>History</strong>
            </span>
          </a>
        </div>
      </div>

  </div>

  <div class="Box-body d-flex flex-items-center flex-auto border-bottom-0 flex-wrap">
    <details class="details-reset details-overlay details-overlay-dark lh-default color-text-primary float-left mr-3" id="blob_contributors_box">
      <summary class="Link--primary" role="button">
        <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-people text-gray">
    <path fill-rule="evenodd" d="M5.5 3.5a2 2 0 100 4 2 2 0 000-4zM2 5.5a3.5 3.5 0 115.898 2.549 5.507 5.507 0 013.034 4.084.75.75 0 11-1.482.235 4.001 4.001 0 00-7.9 0 .75.75 0 01-1.482-.236A5.507 5.507 0 013.102 8.05 3.49 3.49 0 012 5.5zM11 4a.75.75 0 100 1.5 1.5 1.5 0 01.666 2.844.75.75 0 00-.416.672v.352a.75.75 0 00.574.73c1.2.289 2.162 1.2 2.522 2.372a.75.75 0 101.434-.44 5.01 5.01 0 00-2.56-3.012A3 3 0 0011 4z"></path>
</svg>
        <strong>3</strong>
        
        contributors
      </summary>
      <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast" aria-label="Users who have contributed to this file" src="/aws/amazon-sagemaker-examples/contributors-list/master/sagemaker-python-sdk/scikit_learn_inference_pipeline/sklearn_abalone_featurizer.py" preload="" role="dialog" aria-modal="true">
        <div class="Box-header">
          <button class="Box-btn-octicon btn-octicon float-right" type="button" aria-label="Close dialog" data-close-dialog="">
            <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-x">
    <path fill-rule="evenodd" d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z"></path>
</svg>
          </button>
          <h3 class="Box-title">
            Users who have contributed to this file
          </h3>
        </div>
        <include-fragment>
          <svg style="box-sizing: content-box; color: var(--color-icon-primary); --darkreader-inline-fill:none; --darkreader-inline-color:var(--darkreader-text--color-icon-primary);" viewBox="0 0 16 16" fill="none" data-view-component="true" width="32" height="32" class="my-3 mx-auto d-block anim-rotate" data-darkreader-inline-fill="" data-darkreader-inline-color="">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" data-darkreader-inline-stroke="" style="--darkreader-inline-stroke:currentColor;"></circle>
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke" data-darkreader-inline-stroke="" style="--darkreader-inline-stroke:currentColor;"></path>
</svg>
        </include-fragment>
      </details-dialog>
    </details>
      <span class="">
    <a class="avatar-link" data-hovercard-type="user" data-hovercard-url="/users/ajaykarpur/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/aws/amazon-sagemaker-examples/commits/master/sagemaker-python-sdk/scikit_learn_inference_pipeline/sklearn_abalone_featurizer.py?author=ajaykarpur">
      <img class="avatar mr-2 avatar-user" src="./sklearn_abalone_featurizer_files/5490371" width="24" height="24" alt="@ajaykarpur"> 
</a>    <a class="avatar-link" data-hovercard-type="user" data-hovercard-url="/users/ericangelokim/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/aws/amazon-sagemaker-examples/commits/master/sagemaker-python-sdk/scikit_learn_inference_pipeline/sklearn_abalone_featurizer.py?author=ericangelokim">
      <img class="avatar mr-2 avatar-user" src="./sklearn_abalone_featurizer_files/39601338" width="24" height="24" alt="@ericangelokim"> 
</a>    <a class="avatar-link" data-hovercard-type="user" data-hovercard-url="/users/jesterhazy/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/aws/amazon-sagemaker-examples/commits/master/sagemaker-python-sdk/scikit_learn_inference_pipeline/sklearn_abalone_featurizer.py?author=jesterhazy">
      <img class="avatar mr-2 avatar-user" src="./sklearn_abalone_featurizer_files/505258" width="24" height="24" alt="@jesterhazy"> 
</a>
</span>

  </div>
    </div>








  
    <div data-target="readme-toc.content" class="Box mt-3 position-relative
    ">
      
  <div class="Box-header py-2 pr-2 d-flex flex-shrink-0 flex-md-row flex-items-center">


  <div class="text-mono f6 flex-auto pr-3 flex-order-2 flex-md-order-1">
      



      202 lines (162 sloc)
      <span class="file-info-divider"></span>
    6.7 KB
  </div>

  <div class="d-flex py-1 py-md-0 flex-auto flex-order-1 flex-md-order-2 flex-sm-grow-0 flex-justify-between hide-sm hide-md">

    <div class="BtnGroup">
      <a href="https://github.com/aws/amazon-sagemaker-examples/raw/master/sagemaker-python-sdk/scikit_learn_inference_pipeline/sklearn_abalone_featurizer.py" id="raw-url" role="button" data-view-component="true" class="btn-sm btn BtnGroup-item">
  
  Raw
  

</a>
        <a href="https://github.com/aws/amazon-sagemaker-examples/blame/master/sagemaker-python-sdk/scikit_learn_inference_pipeline/sklearn_abalone_featurizer.py" data-hotkey="b" role="button" data-view-component="true" class="js-update-url-with-hash btn-sm btn BtnGroup-item">
  
  Blame
  

</a>
    </div>

    <div>
          <a class="btn-octicon tooltipped tooltipped-nw js-remove-unless-platform" data-platforms="windows,mac" href="https://desktop.github.com/" aria-label="Open this file in GitHub Desktop" data-ga-click="Repository, open with desktop">
              <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-device-desktop">
    <path fill-rule="evenodd" d="M1.75 2.5h12.5a.25.25 0 01.25.25v7.5a.25.25 0 01-.25.25H1.75a.25.25 0 01-.25-.25v-7.5a.25.25 0 01.25-.25zM14.25 1H1.75A1.75 1.75 0 000 2.75v7.5C0 11.216.784 12 1.75 12h3.727c-.1 1.041-.52 1.872-1.292 2.757A.75.75 0 004.75 16h6.5a.75.75 0 00.565-1.243c-.772-.885-1.193-1.716-1.292-2.757h3.727A1.75 1.75 0 0016 10.25v-7.5A1.75 1.75 0 0014.25 1zM9.018 12H6.982a5.72 5.72 0 01-.765 2.5h3.566a5.72 5.72 0 01-.765-2.5z"></path>
</svg>
          </a>

          <a href="https://github.com/login?return_to=%2Faws%2Famazon-sagemaker-examples%2Fblob%2Fmaster%2Fsagemaker-python-sdk%2Fscikit_learn_inference_pipeline%2Fsklearn_abalone_featurizer.py" class="btn-octicon disabled tooltipped tooltipped-nw" aria-label="You must be signed in to make or propose changes">
            <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-pencil">
    <path fill-rule="evenodd" d="M11.013 1.427a1.75 1.75 0 012.474 0l1.086 1.086a1.75 1.75 0 010 2.474l-8.61 8.61c-.21.21-.47.364-.756.445l-3.251.93a.75.75 0 01-.927-.928l.929-3.25a1.75 1.75 0 01.445-.758l8.61-8.61zm1.414 1.06a.25.25 0 00-.354 0L10.811 3.75l1.439 1.44 1.263-1.263a.25.25 0 000-.354l-1.086-1.086zM11.189 6.25L9.75 4.81l-6.286 6.287a.25.25 0 00-.064.108l-.558 1.953 1.953-.558a.249.249 0 00.108-.064l6.286-6.286z"></path>
</svg>
          </a>
          <a href="https://github.com/login?return_to=%2Faws%2Famazon-sagemaker-examples%2Fblob%2Fmaster%2Fsagemaker-python-sdk%2Fscikit_learn_inference_pipeline%2Fsklearn_abalone_featurizer.py" class="btn-octicon btn-octicon-danger disabled tooltipped tooltipped-nw" aria-label="You must be signed in to make or propose changes">
            <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-trash">
    <path fill-rule="evenodd" d="M6.5 1.75a.25.25 0 01.25-.25h2.5a.25.25 0 01.25.25V3h-3V1.75zm4.5 0V3h2.25a.75.75 0 010 1.5H2.75a.75.75 0 010-1.5H5V1.75C5 .784 5.784 0 6.75 0h2.5C10.216 0 11 .784 11 1.75zM4.496 6.675a.75.75 0 10-1.492.15l.66 6.6A1.75 1.75 0 005.405 15h5.19c.9 0 1.652-.681 1.741-1.576l.66-6.6a.75.75 0 00-1.492-.149l-.66 6.6a.25.25 0 01-.249.225h-5.19a.25.25 0 01-.249-.225l-.66-6.6z"></path>
</svg>
          </a>
    </div>
  </div>

    <div class="d-flex hide-lg hide-xl flex-order-2 flex-grow-0">
      <details class="dropdown details-reset details-overlay d-inline-block">
        <summary class="btn-octicon" aria-haspopup="true" aria-label="possible actions">
          <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-kebab-horizontal">
    <path d="M8 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zM1.5 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zm13 0a1.5 1.5 0 100-3 1.5 1.5 0 000 3z"></path>
</svg>
        </summary>

        <ul class="dropdown-menu dropdown-menu-sw">
            <li>
                <a class="dropdown-item tooltipped tooltipped-nw js-remove-unless-platform" data-platforms="windows,mac" href="https://desktop.github.com/" data-ga-click="Repository, open with desktop">
                  Open with Desktop
                </a>
            </li>
          <li>
            <a class="dropdown-item" href="https://github.com/aws/amazon-sagemaker-examples/raw/master/sagemaker-python-sdk/scikit_learn_inference_pipeline/sklearn_abalone_featurizer.py">
              View raw
            </a>
          </li>
            <li>
              <a class="dropdown-item" href="https://github.com/aws/amazon-sagemaker-examples/blame/master/sagemaker-python-sdk/scikit_learn_inference_pipeline/sklearn_abalone_featurizer.py">
                View blame
              </a>
            </li>

        </ul>
      </details>
    </div>
</div>


      
  <div itemprop="text" class="Box-body p-0 blob-wrapper data type-python  gist-border-0">

      
<table class="highlight tab-size js-file-line-container" data-tab-size="8" data-paste-markdown-skip="">
      <tbody><tr>
        <td id="L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="LC1" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> __future__ <span class="pl-k">import</span> <span class="pl-s1">print_function</span></td>
      </tr>
      <tr>
        <td id="L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="LC2" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="LC3" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> <span class="pl-s1">argparse</span></td>
      </tr>
      <tr>
        <td id="L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="LC4" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> <span class="pl-s1">csv</span></td>
      </tr>
      <tr>
        <td id="L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="LC5" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> <span class="pl-s1">json</span></td>
      </tr>
      <tr>
        <td id="L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="LC6" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> <span class="pl-s1">os</span></td>
      </tr>
      <tr>
        <td id="L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="LC7" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> <span class="pl-s1">shutil</span></td>
      </tr>
      <tr>
        <td id="L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="LC8" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> <span class="pl-s1">sys</span></td>
      </tr>
      <tr>
        <td id="L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="LC9" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> <span class="pl-s1">time</span></td>
      </tr>
      <tr>
        <td id="L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="LC10" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> <span class="pl-s1">io</span> <span class="pl-k">import</span> <span class="pl-v">StringIO</span></td>
      </tr>
      <tr>
        <td id="L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="LC11" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="LC12" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> <span class="pl-s1">joblib</span></td>
      </tr>
      <tr>
        <td id="L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="LC13" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> <span class="pl-s1">numpy</span> <span class="pl-k">as</span> <span class="pl-s1">np</span></td>
      </tr>
      <tr>
        <td id="L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="LC14" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> <span class="pl-s1">pandas</span> <span class="pl-k">as</span> <span class="pl-s1">pd</span></td>
      </tr>
      <tr>
        <td id="L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="LC15" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> <span class="pl-s1">sagemaker_containers</span>.<span class="pl-s1">beta</span>.<span class="pl-s1">framework</span> <span class="pl-k">import</span> (</td>
      </tr>
      <tr>
        <td id="L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="LC16" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">content_types</span>,</td>
      </tr>
      <tr>
        <td id="L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="LC17" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">encoders</span>,</td>
      </tr>
      <tr>
        <td id="L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="LC18" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">env</span>,</td>
      </tr>
      <tr>
        <td id="L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="LC19" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">modules</span>,</td>
      </tr>
      <tr>
        <td id="L20" class="blob-num js-line-number" data-line-number="20"></td>
        <td id="LC20" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">transformer</span>,</td>
      </tr>
      <tr>
        <td id="L21" class="blob-num js-line-number" data-line-number="21"></td>
        <td id="LC21" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">worker</span>,</td>
      </tr>
      <tr>
        <td id="L22" class="blob-num js-line-number" data-line-number="22"></td>
        <td id="LC22" class="blob-code blob-code-inner js-file-line">)</td>
      </tr>
      <tr>
        <td id="L23" class="blob-num js-line-number" data-line-number="23"></td>
        <td id="LC23" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> <span class="pl-s1">sklearn</span>.<span class="pl-s1">compose</span> <span class="pl-k">import</span> <span class="pl-v">ColumnTransformer</span>, <span class="pl-s1">make_column_selector</span></td>
      </tr>
      <tr>
        <td id="L24" class="blob-num js-line-number" data-line-number="24"></td>
        <td id="LC24" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> <span class="pl-s1">sklearn</span>.<span class="pl-s1">impute</span> <span class="pl-k">import</span> <span class="pl-v">SimpleImputer</span></td>
      </tr>
      <tr>
        <td id="L25" class="blob-num js-line-number" data-line-number="25"></td>
        <td id="LC25" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> <span class="pl-s1">sklearn</span>.<span class="pl-s1">pipeline</span> <span class="pl-k">import</span> <span class="pl-s1">make_pipeline</span></td>
      </tr>
      <tr>
        <td id="L26" class="blob-num js-line-number" data-line-number="26"></td>
        <td id="LC26" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> <span class="pl-s1">sklearn</span>.<span class="pl-s1">preprocessing</span> <span class="pl-k">import</span> <span class="pl-v">Binarizer</span>, <span class="pl-v">OneHotEncoder</span>, <span class="pl-v">StandardScaler</span></td>
      </tr>
      <tr>
        <td id="L27" class="blob-num js-line-number" data-line-number="27"></td>
        <td id="LC27" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L28" class="blob-num js-line-number" data-line-number="28"></td>
        <td id="LC28" class="blob-code blob-code-inner js-file-line"><span class="pl-c"># Since we get a headerless CSV file we specify the column names here.</span></td>
      </tr>
      <tr>
        <td id="L29" class="blob-num js-line-number" data-line-number="29"></td>
        <td id="LC29" class="blob-code blob-code-inner js-file-line"><span class="pl-s1">feature_columns_names</span> <span class="pl-c1">=</span> [</td>
      </tr>
      <tr>
        <td id="L30" class="blob-num js-line-number" data-line-number="30"></td>
        <td id="LC30" class="blob-code blob-code-inner js-file-line">    <span class="pl-s">"sex"</span>,  <span class="pl-c"># M, F, and I (infant)</span></td>
      </tr>
      <tr>
        <td id="L31" class="blob-num js-line-number" data-line-number="31"></td>
        <td id="LC31" class="blob-code blob-code-inner js-file-line">    <span class="pl-s">"length"</span>,  <span class="pl-c"># Longest shell measurement</span></td>
      </tr>
      <tr>
        <td id="L32" class="blob-num js-line-number" data-line-number="32"></td>
        <td id="LC32" class="blob-code blob-code-inner js-file-line">    <span class="pl-s">"diameter"</span>,  <span class="pl-c"># perpendicular to length</span></td>
      </tr>
      <tr>
        <td id="L33" class="blob-num js-line-number" data-line-number="33"></td>
        <td id="LC33" class="blob-code blob-code-inner js-file-line">    <span class="pl-s">"height"</span>,  <span class="pl-c"># with meat in shell</span></td>
      </tr>
      <tr>
        <td id="L34" class="blob-num js-line-number" data-line-number="34"></td>
        <td id="LC34" class="blob-code blob-code-inner js-file-line">    <span class="pl-s">"whole_weight"</span>,  <span class="pl-c"># whole abalone</span></td>
      </tr>
      <tr>
        <td id="L35" class="blob-num js-line-number" data-line-number="35"></td>
        <td id="LC35" class="blob-code blob-code-inner js-file-line">    <span class="pl-s">"shucked_weight"</span>,  <span class="pl-c"># weight of meat</span></td>
      </tr>
      <tr>
        <td id="L36" class="blob-num js-line-number" data-line-number="36"></td>
        <td id="LC36" class="blob-code blob-code-inner js-file-line">    <span class="pl-s">"viscera_weight"</span>,  <span class="pl-c"># gut weight (after bleeding)</span></td>
      </tr>
      <tr>
        <td id="L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="LC37" class="blob-code blob-code-inner js-file-line">    <span class="pl-s">"shell_weight"</span>,</td>
      </tr>
      <tr>
        <td id="L38" class="blob-num js-line-number" data-line-number="38"></td>
        <td id="LC38" class="blob-code blob-code-inner js-file-line">]  <span class="pl-c"># after being dried</span></td>
      </tr>
      <tr>
        <td id="L39" class="blob-num js-line-number" data-line-number="39"></td>
        <td id="LC39" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L40" class="blob-num js-line-number" data-line-number="40"></td>
        <td id="LC40" class="blob-code blob-code-inner js-file-line"><span class="pl-s1">label_column</span> <span class="pl-c1">=</span> <span class="pl-s">"rings"</span></td>
      </tr>
      <tr>
        <td id="L41" class="blob-num js-line-number" data-line-number="41"></td>
        <td id="LC41" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L42" class="blob-num js-line-number" data-line-number="42"></td>
        <td id="LC42" class="blob-code blob-code-inner js-file-line"><span class="pl-s1">feature_columns_dtype</span> <span class="pl-c1">=</span> {</td>
      </tr>
      <tr>
        <td id="L43" class="blob-num js-line-number" data-line-number="43"></td>
        <td id="LC43" class="blob-code blob-code-inner js-file-line">    <span class="pl-s">"sex"</span>: <span class="pl-s">"category"</span>,</td>
      </tr>
      <tr>
        <td id="L44" class="blob-num js-line-number" data-line-number="44"></td>
        <td id="LC44" class="blob-code blob-code-inner js-file-line">    <span class="pl-s">"length"</span>: <span class="pl-s">"float64"</span>,</td>
      </tr>
      <tr>
        <td id="L45" class="blob-num js-line-number" data-line-number="45"></td>
        <td id="LC45" class="blob-code blob-code-inner js-file-line">    <span class="pl-s">"diameter"</span>: <span class="pl-s">"float64"</span>,</td>
      </tr>
      <tr>
        <td id="L46" class="blob-num js-line-number" data-line-number="46"></td>
        <td id="LC46" class="blob-code blob-code-inner js-file-line">    <span class="pl-s">"height"</span>: <span class="pl-s">"float64"</span>,</td>
      </tr>
      <tr>
        <td id="L47" class="blob-num js-line-number" data-line-number="47"></td>
        <td id="LC47" class="blob-code blob-code-inner js-file-line">    <span class="pl-s">"whole_weight"</span>: <span class="pl-s">"float64"</span>,</td>
      </tr>
      <tr>
        <td id="L48" class="blob-num js-line-number" data-line-number="48"></td>
        <td id="LC48" class="blob-code blob-code-inner js-file-line">    <span class="pl-s">"shucked_weight"</span>: <span class="pl-s">"float64"</span>,</td>
      </tr>
      <tr>
        <td id="L49" class="blob-num js-line-number" data-line-number="49"></td>
        <td id="LC49" class="blob-code blob-code-inner js-file-line">    <span class="pl-s">"viscera_weight"</span>: <span class="pl-s">"float64"</span>,</td>
      </tr>
      <tr>
        <td id="L50" class="blob-num js-line-number" data-line-number="50"></td>
        <td id="LC50" class="blob-code blob-code-inner js-file-line">    <span class="pl-s">"shell_weight"</span>: <span class="pl-s">"float64"</span>,</td>
      </tr>
      <tr>
        <td id="L51" class="blob-num js-line-number" data-line-number="51"></td>
        <td id="LC51" class="blob-code blob-code-inner js-file-line">}</td>
      </tr>
      <tr>
        <td id="L52" class="blob-num js-line-number" data-line-number="52"></td>
        <td id="LC52" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L53" class="blob-num js-line-number" data-line-number="53"></td>
        <td id="LC53" class="blob-code blob-code-inner js-file-line"><span class="pl-s1">label_column_dtype</span> <span class="pl-c1">=</span> {<span class="pl-s">"rings"</span>: <span class="pl-s">"float64"</span>}  <span class="pl-c"># +1.5 gives the age in years</span></td>
      </tr>
      <tr>
        <td id="L54" class="blob-num js-line-number" data-line-number="54"></td>
        <td id="LC54" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L55" class="blob-num js-line-number" data-line-number="55"></td>
        <td id="LC55" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L56" class="blob-num js-line-number" data-line-number="56"></td>
        <td id="LC56" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">merge_two_dicts</span>(<span class="pl-s1">x</span>, <span class="pl-s1">y</span>):</td>
      </tr>
      <tr>
        <td id="L57" class="blob-num js-line-number" data-line-number="57"></td>
        <td id="LC57" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">z</span> <span class="pl-c1">=</span> <span class="pl-s1">x</span>.<span class="pl-en">copy</span>()  <span class="pl-c"># start with x's keys and values</span></td>
      </tr>
      <tr>
        <td id="L58" class="blob-num js-line-number" data-line-number="58"></td>
        <td id="LC58" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">z</span>.<span class="pl-en">update</span>(<span class="pl-s1">y</span>)  <span class="pl-c"># modifies z with y's keys and values &amp; returns None</span></td>
      </tr>
      <tr>
        <td id="L59" class="blob-num js-line-number" data-line-number="59"></td>
        <td id="LC59" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> <span class="pl-s1">z</span></td>
      </tr>
      <tr>
        <td id="L60" class="blob-num js-line-number" data-line-number="60"></td>
        <td id="LC60" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L61" class="blob-num js-line-number" data-line-number="61"></td>
        <td id="LC61" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L62" class="blob-num js-line-number" data-line-number="62"></td>
        <td id="LC62" class="blob-code blob-code-inner js-file-line"><span class="pl-k">if</span> <span class="pl-s1">__name__</span> <span class="pl-c1">==</span> <span class="pl-s">"__main__"</span>:</td>
      </tr>
      <tr>
        <td id="L63" class="blob-num js-line-number" data-line-number="63"></td>
        <td id="LC63" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L64" class="blob-num js-line-number" data-line-number="64"></td>
        <td id="LC64" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">parser</span> <span class="pl-c1">=</span> <span class="pl-s1">argparse</span>.<span class="pl-v">ArgumentParser</span>()</td>
      </tr>
      <tr>
        <td id="L65" class="blob-num js-line-number" data-line-number="65"></td>
        <td id="LC65" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L66" class="blob-num js-line-number" data-line-number="66"></td>
        <td id="LC66" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># Sagemaker specific arguments. Defaults are set in the environment variables.</span></td>
      </tr>
      <tr>
        <td id="L67" class="blob-num js-line-number" data-line-number="67"></td>
        <td id="LC67" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">parser</span>.<span class="pl-en">add_argument</span>(<span class="pl-s">"--output-data-dir"</span>, <span class="pl-s1">type</span><span class="pl-c1">=</span><span class="pl-s1">str</span>, <span class="pl-s1">default</span><span class="pl-c1">=</span><span class="pl-s1">os</span>.<span class="pl-s1">environ</span>[<span class="pl-s">"SM_OUTPUT_DATA_DIR"</span>])</td>
      </tr>
      <tr>
        <td id="L68" class="blob-num js-line-number" data-line-number="68"></td>
        <td id="LC68" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">parser</span>.<span class="pl-en">add_argument</span>(<span class="pl-s">"--model-dir"</span>, <span class="pl-s1">type</span><span class="pl-c1">=</span><span class="pl-s1">str</span>, <span class="pl-s1">default</span><span class="pl-c1">=</span><span class="pl-s1">os</span>.<span class="pl-s1">environ</span>[<span class="pl-s">"SM_MODEL_DIR"</span>])</td>
      </tr>
      <tr>
        <td id="L69" class="blob-num js-line-number" data-line-number="69"></td>
        <td id="LC69" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">parser</span>.<span class="pl-en">add_argument</span>(<span class="pl-s">"--train"</span>, <span class="pl-s1">type</span><span class="pl-c1">=</span><span class="pl-s1">str</span>, <span class="pl-s1">default</span><span class="pl-c1">=</span><span class="pl-s1">os</span>.<span class="pl-s1">environ</span>[<span class="pl-s">"SM_CHANNEL_TRAIN"</span>])</td>
      </tr>
      <tr>
        <td id="L70" class="blob-num js-line-number" data-line-number="70"></td>
        <td id="LC70" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L71" class="blob-num js-line-number" data-line-number="71"></td>
        <td id="LC71" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">args</span> <span class="pl-c1">=</span> <span class="pl-s1">parser</span>.<span class="pl-en">parse_args</span>()</td>
      </tr>
      <tr>
        <td id="L72" class="blob-num js-line-number" data-line-number="72"></td>
        <td id="LC72" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L73" class="blob-num js-line-number" data-line-number="73"></td>
        <td id="LC73" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># Take the set of files and read them all into a single pandas dataframe</span></td>
      </tr>
      <tr>
        <td id="L74" class="blob-num js-line-number" data-line-number="74"></td>
        <td id="LC74" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">input_files</span> <span class="pl-c1">=</span> [<span class="pl-s1">os</span>.<span class="pl-s1">path</span>.<span class="pl-en">join</span>(<span class="pl-s1">args</span>.<span class="pl-s1">train</span>, <span class="pl-s1">file</span>) <span class="pl-k">for</span> <span class="pl-s1">file</span> <span class="pl-c1">in</span> <span class="pl-s1">os</span>.<span class="pl-en">listdir</span>(<span class="pl-s1">args</span>.<span class="pl-s1">train</span>)]</td>
      </tr>
      <tr>
        <td id="L75" class="blob-num js-line-number" data-line-number="75"></td>
        <td id="LC75" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-en">len</span>(<span class="pl-s1">input_files</span>) <span class="pl-c1">==</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L76" class="blob-num js-line-number" data-line-number="76"></td>
        <td id="LC76" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">raise</span> <span class="pl-v">ValueError</span>(</td>
      </tr>
      <tr>
        <td id="L77" class="blob-num js-line-number" data-line-number="77"></td>
        <td id="LC77" class="blob-code blob-code-inner js-file-line">            (</td>
      </tr>
      <tr>
        <td id="L78" class="blob-num js-line-number" data-line-number="78"></td>
        <td id="LC78" class="blob-code blob-code-inner js-file-line">                <span class="pl-s">"There are no files in {}.<span class="pl-cce">\n</span>"</span></td>
      </tr>
      <tr>
        <td id="L79" class="blob-num js-line-number" data-line-number="79"></td>
        <td id="LC79" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">+</span> <span class="pl-s">"This usually indicates that the channel ({}) was incorrectly specified,<span class="pl-cce">\n</span>"</span></td>
      </tr>
      <tr>
        <td id="L80" class="blob-num js-line-number" data-line-number="80"></td>
        <td id="LC80" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">+</span> <span class="pl-s">"the data specification in S3 was incorrectly specified or the role specified<span class="pl-cce">\n</span>"</span></td>
      </tr>
      <tr>
        <td id="L81" class="blob-num js-line-number" data-line-number="81"></td>
        <td id="LC81" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">+</span> <span class="pl-s">"does not have permission to access the data."</span></td>
      </tr>
      <tr>
        <td id="L82" class="blob-num js-line-number" data-line-number="82"></td>
        <td id="LC82" class="blob-code blob-code-inner js-file-line">            ).<span class="pl-en">format</span>(<span class="pl-s1">args</span>.<span class="pl-s1">train</span>, <span class="pl-s">"train"</span>)</td>
      </tr>
      <tr>
        <td id="L83" class="blob-num js-line-number" data-line-number="83"></td>
        <td id="LC83" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L84" class="blob-num js-line-number" data-line-number="84"></td>
        <td id="LC84" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L85" class="blob-num js-line-number" data-line-number="85"></td>
        <td id="LC85" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">raw_data</span> <span class="pl-c1">=</span> [</td>
      </tr>
      <tr>
        <td id="L86" class="blob-num js-line-number" data-line-number="86"></td>
        <td id="LC86" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">pd</span>.<span class="pl-en">read_csv</span>(</td>
      </tr>
      <tr>
        <td id="L87" class="blob-num js-line-number" data-line-number="87"></td>
        <td id="LC87" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">file</span>,</td>
      </tr>
      <tr>
        <td id="L88" class="blob-num js-line-number" data-line-number="88"></td>
        <td id="LC88" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">header</span><span class="pl-c1">=</span><span class="pl-c1">None</span>,</td>
      </tr>
      <tr>
        <td id="L89" class="blob-num js-line-number" data-line-number="89"></td>
        <td id="LC89" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">names</span><span class="pl-c1">=</span><span class="pl-s1">feature_columns_names</span> <span class="pl-c1">+</span> [<span class="pl-s1">label_column</span>],</td>
      </tr>
      <tr>
        <td id="L90" class="blob-num js-line-number" data-line-number="90"></td>
        <td id="LC90" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">dtype</span><span class="pl-c1">=</span><span class="pl-en">merge_two_dicts</span>(<span class="pl-s1">feature_columns_dtype</span>, <span class="pl-s1">label_column_dtype</span>),</td>
      </tr>
      <tr>
        <td id="L91" class="blob-num js-line-number" data-line-number="91"></td>
        <td id="LC91" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L92" class="blob-num js-line-number" data-line-number="92"></td>
        <td id="LC92" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> <span class="pl-s1">file</span> <span class="pl-c1">in</span> <span class="pl-s1">input_files</span></td>
      </tr>
      <tr>
        <td id="L93" class="blob-num js-line-number" data-line-number="93"></td>
        <td id="LC93" class="blob-code blob-code-inner js-file-line">    ]</td>
      </tr>
      <tr>
        <td id="L94" class="blob-num js-line-number" data-line-number="94"></td>
        <td id="LC94" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">concat_data</span> <span class="pl-c1">=</span> <span class="pl-s1">pd</span>.<span class="pl-en">concat</span>(<span class="pl-s1">raw_data</span>)</td>
      </tr>
      <tr>
        <td id="L95" class="blob-num js-line-number" data-line-number="95"></td>
        <td id="LC95" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L96" class="blob-num js-line-number" data-line-number="96"></td>
        <td id="LC96" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># Labels should not be preprocessed. predict_fn will reinsert the labels after featurizing.</span></td>
      </tr>
      <tr>
        <td id="L97" class="blob-num js-line-number" data-line-number="97"></td>
        <td id="LC97" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">concat_data</span>.<span class="pl-en">drop</span>(<span class="pl-s1">label_column</span>, <span class="pl-s1">axis</span><span class="pl-c1">=</span><span class="pl-c1">1</span>, <span class="pl-s1">inplace</span><span class="pl-c1">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L98" class="blob-num js-line-number" data-line-number="98"></td>
        <td id="LC98" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L99" class="blob-num js-line-number" data-line-number="99"></td>
        <td id="LC99" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># This section is adapted from the scikit-learn example of using preprocessing pipelines:</span></td>
      </tr>
      <tr>
        <td id="L100" class="blob-num js-line-number" data-line-number="100"></td>
        <td id="LC100" class="blob-code blob-code-inner js-file-line">    <span class="pl-c">#</span></td>
      </tr>
      <tr>
        <td id="L101" class="blob-num js-line-number" data-line-number="101"></td>
        <td id="LC101" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer_mixed_types.html</span></td>
      </tr>
      <tr>
        <td id="L102" class="blob-num js-line-number" data-line-number="102"></td>
        <td id="LC102" class="blob-code blob-code-inner js-file-line">    <span class="pl-c">#</span></td>
      </tr>
      <tr>
        <td id="L103" class="blob-num js-line-number" data-line-number="103"></td>
        <td id="LC103" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># We will train our classifier with the following features:</span></td>
      </tr>
      <tr>
        <td id="L104" class="blob-num js-line-number" data-line-number="104"></td>
        <td id="LC104" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># Numeric Features:</span></td>
      </tr>
      <tr>
        <td id="L105" class="blob-num js-line-number" data-line-number="105"></td>
        <td id="LC105" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># - length:  Longest shell measurement</span></td>
      </tr>
      <tr>
        <td id="L106" class="blob-num js-line-number" data-line-number="106"></td>
        <td id="LC106" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># - diameter: Diameter perpendicular to length</span></td>
      </tr>
      <tr>
        <td id="L107" class="blob-num js-line-number" data-line-number="107"></td>
        <td id="LC107" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># - height:  Height with meat in shell</span></td>
      </tr>
      <tr>
        <td id="L108" class="blob-num js-line-number" data-line-number="108"></td>
        <td id="LC108" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># - whole_weight: Weight of whole abalone</span></td>
      </tr>
      <tr>
        <td id="L109" class="blob-num js-line-number" data-line-number="109"></td>
        <td id="LC109" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># - shucked_weight: Weight of meat</span></td>
      </tr>
      <tr>
        <td id="L110" class="blob-num js-line-number" data-line-number="110"></td>
        <td id="LC110" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># - viscera_weight: Gut weight (after bleeding)</span></td>
      </tr>
      <tr>
        <td id="L111" class="blob-num js-line-number" data-line-number="111"></td>
        <td id="LC111" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># - shell_weight: Weight after being dried</span></td>
      </tr>
      <tr>
        <td id="L112" class="blob-num js-line-number" data-line-number="112"></td>
        <td id="LC112" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># Categorical Features:</span></td>
      </tr>
      <tr>
        <td id="L113" class="blob-num js-line-number" data-line-number="113"></td>
        <td id="LC113" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"># - sex: categories encoded as strings {'M', 'F', 'I'} where 'I' is Infant</span></td>
      </tr>
      <tr>
        <td id="L114" class="blob-num js-line-number" data-line-number="114"></td>
        <td id="LC114" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">numeric_transformer</span> <span class="pl-c1">=</span> <span class="pl-en">make_pipeline</span>(<span class="pl-v">SimpleImputer</span>(<span class="pl-s1">strategy</span><span class="pl-c1">=</span><span class="pl-s">"median"</span>), <span class="pl-v">StandardScaler</span>())</td>
      </tr>
      <tr>
        <td id="L115" class="blob-num js-line-number" data-line-number="115"></td>
        <td id="LC115" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L116" class="blob-num js-line-number" data-line-number="116"></td>
        <td id="LC116" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">categorical_transformer</span> <span class="pl-c1">=</span> <span class="pl-en">make_pipeline</span>(</td>
      </tr>
      <tr>
        <td id="L117" class="blob-num js-line-number" data-line-number="117"></td>
        <td id="LC117" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">SimpleImputer</span>(<span class="pl-s1">strategy</span><span class="pl-c1">=</span><span class="pl-s">"constant"</span>, <span class="pl-s1">fill_value</span><span class="pl-c1">=</span><span class="pl-s">"missing"</span>),</td>
      </tr>
      <tr>
        <td id="L118" class="blob-num js-line-number" data-line-number="118"></td>
        <td id="LC118" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">OneHotEncoder</span>(<span class="pl-s1">handle_unknown</span><span class="pl-c1">=</span><span class="pl-s">"ignore"</span>),</td>
      </tr>
      <tr>
        <td id="L119" class="blob-num js-line-number" data-line-number="119"></td>
        <td id="LC119" class="blob-code blob-code-inner js-file-line">    )</td>
      </tr>
      <tr>
        <td id="L120" class="blob-num js-line-number" data-line-number="120"></td>
        <td id="LC120" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L121" class="blob-num js-line-number" data-line-number="121"></td>
        <td id="LC121" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">preprocessor</span> <span class="pl-c1">=</span> <span class="pl-v">ColumnTransformer</span>(</td>
      </tr>
      <tr>
        <td id="L122" class="blob-num js-line-number" data-line-number="122"></td>
        <td id="LC122" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">transformers</span><span class="pl-c1">=</span>[</td>
      </tr>
      <tr>
        <td id="L123" class="blob-num js-line-number" data-line-number="123"></td>
        <td id="LC123" class="blob-code blob-code-inner js-file-line">            (<span class="pl-s">"num"</span>, <span class="pl-s1">numeric_transformer</span>, <span class="pl-en">make_column_selector</span>(<span class="pl-s1">dtype_exclude</span><span class="pl-c1">=</span><span class="pl-s">"category"</span>)),</td>
      </tr>
      <tr>
        <td id="L124" class="blob-num js-line-number" data-line-number="124"></td>
        <td id="LC124" class="blob-code blob-code-inner js-file-line">            (<span class="pl-s">"cat"</span>, <span class="pl-s1">categorical_transformer</span>, <span class="pl-en">make_column_selector</span>(<span class="pl-s1">dtype_include</span><span class="pl-c1">=</span><span class="pl-s">"category"</span>)),</td>
      </tr>
      <tr>
        <td id="L125" class="blob-num js-line-number" data-line-number="125"></td>
        <td id="LC125" class="blob-code blob-code-inner js-file-line">        ]</td>
      </tr>
      <tr>
        <td id="L126" class="blob-num js-line-number" data-line-number="126"></td>
        <td id="LC126" class="blob-code blob-code-inner js-file-line">    )</td>
      </tr>
      <tr>
        <td id="L127" class="blob-num js-line-number" data-line-number="127"></td>
        <td id="LC127" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L128" class="blob-num js-line-number" data-line-number="128"></td>
        <td id="LC128" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">preprocessor</span>.<span class="pl-en">fit</span>(<span class="pl-s1">concat_data</span>)</td>
      </tr>
      <tr>
        <td id="L129" class="blob-num js-line-number" data-line-number="129"></td>
        <td id="LC129" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L130" class="blob-num js-line-number" data-line-number="130"></td>
        <td id="LC130" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">joblib</span>.<span class="pl-en">dump</span>(<span class="pl-s1">preprocessor</span>, <span class="pl-s1">os</span>.<span class="pl-s1">path</span>.<span class="pl-en">join</span>(<span class="pl-s1">args</span>.<span class="pl-s1">model_dir</span>, <span class="pl-s">"model.joblib"</span>))</td>
      </tr>
      <tr>
        <td id="L131" class="blob-num js-line-number" data-line-number="131"></td>
        <td id="LC131" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L132" class="blob-num js-line-number" data-line-number="132"></td>
        <td id="LC132" class="blob-code blob-code-inner js-file-line">    <span class="pl-en">print</span>(<span class="pl-s">"saved model!"</span>)</td>
      </tr>
      <tr>
        <td id="L133" class="blob-num js-line-number" data-line-number="133"></td>
        <td id="LC133" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L134" class="blob-num js-line-number" data-line-number="134"></td>
        <td id="LC134" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L135" class="blob-num js-line-number" data-line-number="135"></td>
        <td id="LC135" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">input_fn</span>(<span class="pl-s1">input_data</span>, <span class="pl-s1">content_type</span>):</td>
      </tr>
      <tr>
        <td id="L136" class="blob-num js-line-number" data-line-number="136"></td>
        <td id="LC136" class="blob-code blob-code-inner js-file-line">    <span class="pl-s">"""Parse input data payload</span></td>
      </tr>
      <tr>
        <td id="L137" class="blob-num js-line-number" data-line-number="137"></td>
        <td id="LC137" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L138" class="blob-num js-line-number" data-line-number="138"></td>
        <td id="LC138" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    We currently only take csv input. Since we need to process both labelled</span></td>
      </tr>
      <tr>
        <td id="L139" class="blob-num js-line-number" data-line-number="139"></td>
        <td id="LC139" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    and unlabelled data we first determine whether the label column is present</span></td>
      </tr>
      <tr>
        <td id="L140" class="blob-num js-line-number" data-line-number="140"></td>
        <td id="LC140" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    by looking at how many columns were provided.</span></td>
      </tr>
      <tr>
        <td id="L141" class="blob-num js-line-number" data-line-number="141"></td>
        <td id="LC141" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    """</span></td>
      </tr>
      <tr>
        <td id="L142" class="blob-num js-line-number" data-line-number="142"></td>
        <td id="LC142" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-s1">content_type</span> <span class="pl-c1">==</span> <span class="pl-s">"text/csv"</span>:</td>
      </tr>
      <tr>
        <td id="L143" class="blob-num js-line-number" data-line-number="143"></td>
        <td id="LC143" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"># Read the raw input data as CSV.</span></td>
      </tr>
      <tr>
        <td id="L144" class="blob-num js-line-number" data-line-number="144"></td>
        <td id="LC144" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">df</span> <span class="pl-c1">=</span> <span class="pl-s1">pd</span>.<span class="pl-en">read_csv</span>(<span class="pl-v">StringIO</span>(<span class="pl-s1">input_data</span>), <span class="pl-s1">header</span><span class="pl-c1">=</span><span class="pl-c1">None</span>)</td>
      </tr>
      <tr>
        <td id="L145" class="blob-num js-line-number" data-line-number="145"></td>
        <td id="LC145" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L146" class="blob-num js-line-number" data-line-number="146"></td>
        <td id="LC146" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-en">len</span>(<span class="pl-s1">df</span>.<span class="pl-s1">columns</span>) <span class="pl-c1">==</span> <span class="pl-en">len</span>(<span class="pl-s1">feature_columns_names</span>) <span class="pl-c1">+</span> <span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L147" class="blob-num js-line-number" data-line-number="147"></td>
        <td id="LC147" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"># This is a labelled example, includes the ring label</span></td>
      </tr>
      <tr>
        <td id="L148" class="blob-num js-line-number" data-line-number="148"></td>
        <td id="LC148" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">df</span>.<span class="pl-s1">columns</span> <span class="pl-c1">=</span> <span class="pl-s1">feature_columns_names</span> <span class="pl-c1">+</span> [<span class="pl-s1">label_column</span>]</td>
      </tr>
      <tr>
        <td id="L149" class="blob-num js-line-number" data-line-number="149"></td>
        <td id="LC149" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">elif</span> <span class="pl-en">len</span>(<span class="pl-s1">df</span>.<span class="pl-s1">columns</span>) <span class="pl-c1">==</span> <span class="pl-en">len</span>(<span class="pl-s1">feature_columns_names</span>):</td>
      </tr>
      <tr>
        <td id="L150" class="blob-num js-line-number" data-line-number="150"></td>
        <td id="LC150" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"># This is an unlabelled example.</span></td>
      </tr>
      <tr>
        <td id="L151" class="blob-num js-line-number" data-line-number="151"></td>
        <td id="LC151" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">df</span>.<span class="pl-s1">columns</span> <span class="pl-c1">=</span> <span class="pl-s1">feature_columns_names</span></td>
      </tr>
      <tr>
        <td id="L152" class="blob-num js-line-number" data-line-number="152"></td>
        <td id="LC152" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L153" class="blob-num js-line-number" data-line-number="153"></td>
        <td id="LC153" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-s1">df</span></td>
      </tr>
      <tr>
        <td id="L154" class="blob-num js-line-number" data-line-number="154"></td>
        <td id="LC154" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L155" class="blob-num js-line-number" data-line-number="155"></td>
        <td id="LC155" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">raise</span> <span class="pl-v">ValueError</span>(<span class="pl-s">"{} not supported by script!"</span>.<span class="pl-en">format</span>(<span class="pl-s1">content_type</span>))</td>
      </tr>
      <tr>
        <td id="L156" class="blob-num js-line-number" data-line-number="156"></td>
        <td id="LC156" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L157" class="blob-num js-line-number" data-line-number="157"></td>
        <td id="LC157" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L158" class="blob-num js-line-number" data-line-number="158"></td>
        <td id="LC158" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">output_fn</span>(<span class="pl-s1">prediction</span>, <span class="pl-s1">accept</span>):</td>
      </tr>
      <tr>
        <td id="L159" class="blob-num js-line-number" data-line-number="159"></td>
        <td id="LC159" class="blob-code blob-code-inner js-file-line">    <span class="pl-s">"""Format prediction output</span></td>
      </tr>
      <tr>
        <td id="L160" class="blob-num js-line-number" data-line-number="160"></td>
        <td id="LC160" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L161" class="blob-num js-line-number" data-line-number="161"></td>
        <td id="LC161" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    The default accept/content-type between containers for serial inference is JSON.</span></td>
      </tr>
      <tr>
        <td id="L162" class="blob-num js-line-number" data-line-number="162"></td>
        <td id="LC162" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    We also want to set the ContentType or mimetype as the same value as accept so the next</span></td>
      </tr>
      <tr>
        <td id="L163" class="blob-num js-line-number" data-line-number="163"></td>
        <td id="LC163" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    container can read the response payload correctly.</span></td>
      </tr>
      <tr>
        <td id="L164" class="blob-num js-line-number" data-line-number="164"></td>
        <td id="LC164" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    """</span></td>
      </tr>
      <tr>
        <td id="L165" class="blob-num js-line-number" data-line-number="165"></td>
        <td id="LC165" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-s1">accept</span> <span class="pl-c1">==</span> <span class="pl-s">"application/json"</span>:</td>
      </tr>
      <tr>
        <td id="L166" class="blob-num js-line-number" data-line-number="166"></td>
        <td id="LC166" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">instances</span> <span class="pl-c1">=</span> []</td>
      </tr>
      <tr>
        <td id="L167" class="blob-num js-line-number" data-line-number="167"></td>
        <td id="LC167" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> <span class="pl-s1">row</span> <span class="pl-c1">in</span> <span class="pl-s1">prediction</span>.<span class="pl-en">tolist</span>():</td>
      </tr>
      <tr>
        <td id="L168" class="blob-num js-line-number" data-line-number="168"></td>
        <td id="LC168" class="blob-code blob-code-inner js-file-line">            <span class="pl-s1">instances</span>.<span class="pl-en">append</span>({<span class="pl-s">"features"</span>: <span class="pl-s1">row</span>})</td>
      </tr>
      <tr>
        <td id="L169" class="blob-num js-line-number" data-line-number="169"></td>
        <td id="LC169" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L170" class="blob-num js-line-number" data-line-number="170"></td>
        <td id="LC170" class="blob-code blob-code-inner js-file-line">        <span class="pl-s1">json_output</span> <span class="pl-c1">=</span> {<span class="pl-s">"instances"</span>: <span class="pl-s1">instances</span>}</td>
      </tr>
      <tr>
        <td id="L171" class="blob-num js-line-number" data-line-number="171"></td>
        <td id="LC171" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L172" class="blob-num js-line-number" data-line-number="172"></td>
        <td id="LC172" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-s1">worker</span>.<span class="pl-v">Response</span>(<span class="pl-s1">json</span>.<span class="pl-en">dumps</span>(<span class="pl-s1">json_output</span>), <span class="pl-s1">mimetype</span><span class="pl-c1">=</span><span class="pl-s1">accept</span>)</td>
      </tr>
      <tr>
        <td id="L173" class="blob-num js-line-number" data-line-number="173"></td>
        <td id="LC173" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">elif</span> <span class="pl-s1">accept</span> <span class="pl-c1">==</span> <span class="pl-s">"text/csv"</span>:</td>
      </tr>
      <tr>
        <td id="L174" class="blob-num js-line-number" data-line-number="174"></td>
        <td id="LC174" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-s1">worker</span>.<span class="pl-v">Response</span>(<span class="pl-s1">encoders</span>.<span class="pl-en">encode</span>(<span class="pl-s1">prediction</span>, <span class="pl-s1">accept</span>), <span class="pl-s1">mimetype</span><span class="pl-c1">=</span><span class="pl-s1">accept</span>)</td>
      </tr>
      <tr>
        <td id="L175" class="blob-num js-line-number" data-line-number="175"></td>
        <td id="LC175" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L176" class="blob-num js-line-number" data-line-number="176"></td>
        <td id="LC176" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">raise</span> <span class="pl-v">RuntimeException</span>(<span class="pl-s">"{} accept type is not supported by this script."</span>.<span class="pl-en">format</span>(<span class="pl-s1">accept</span>))</td>
      </tr>
      <tr>
        <td id="L177" class="blob-num js-line-number" data-line-number="177"></td>
        <td id="LC177" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L178" class="blob-num js-line-number" data-line-number="178"></td>
        <td id="LC178" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L179" class="blob-num js-line-number" data-line-number="179"></td>
        <td id="LC179" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">predict_fn</span>(<span class="pl-s1">input_data</span>, <span class="pl-s1">model</span>):</td>
      </tr>
      <tr>
        <td id="L180" class="blob-num js-line-number" data-line-number="180"></td>
        <td id="LC180" class="blob-code blob-code-inner js-file-line">    <span class="pl-s">"""Preprocess input data</span></td>
      </tr>
      <tr>
        <td id="L181" class="blob-num js-line-number" data-line-number="181"></td>
        <td id="LC181" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L182" class="blob-num js-line-number" data-line-number="182"></td>
        <td id="LC182" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    We implement this because the default predict_fn uses .predict(), but our model is a preprocessor</span></td>
      </tr>
      <tr>
        <td id="L183" class="blob-num js-line-number" data-line-number="183"></td>
        <td id="LC183" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    so we want to use .transform().</span></td>
      </tr>
      <tr>
        <td id="L184" class="blob-num js-line-number" data-line-number="184"></td>
        <td id="LC184" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L185" class="blob-num js-line-number" data-line-number="185"></td>
        <td id="LC185" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    The output is returned in the following order:</span></td>
      </tr>
      <tr>
        <td id="L186" class="blob-num js-line-number" data-line-number="186"></td>
        <td id="LC186" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L187" class="blob-num js-line-number" data-line-number="187"></td>
        <td id="LC187" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        rest of features either one hot encoded or standardized</span></td>
      </tr>
      <tr>
        <td id="L188" class="blob-num js-line-number" data-line-number="188"></td>
        <td id="LC188" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    """</span></td>
      </tr>
      <tr>
        <td id="L189" class="blob-num js-line-number" data-line-number="189"></td>
        <td id="LC189" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">features</span> <span class="pl-c1">=</span> <span class="pl-s1">model</span>.<span class="pl-en">transform</span>(<span class="pl-s1">input_data</span>)</td>
      </tr>
      <tr>
        <td id="L190" class="blob-num js-line-number" data-line-number="190"></td>
        <td id="LC190" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L191" class="blob-num js-line-number" data-line-number="191"></td>
        <td id="LC191" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-s1">label_column</span> <span class="pl-c1">in</span> <span class="pl-s1">input_data</span>:</td>
      </tr>
      <tr>
        <td id="L192" class="blob-num js-line-number" data-line-number="192"></td>
        <td id="LC192" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"># Return the label (as the first column) and the set of features.</span></td>
      </tr>
      <tr>
        <td id="L193" class="blob-num js-line-number" data-line-number="193"></td>
        <td id="LC193" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-s1">np</span>.<span class="pl-en">insert</span>(<span class="pl-s1">features</span>, <span class="pl-c1">0</span>, <span class="pl-s1">input_data</span>[<span class="pl-s1">label_column</span>], <span class="pl-s1">axis</span><span class="pl-c1">=</span><span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L194" class="blob-num js-line-number" data-line-number="194"></td>
        <td id="LC194" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L195" class="blob-num js-line-number" data-line-number="195"></td>
        <td id="LC195" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"># Return only the set of features</span></td>
      </tr>
      <tr>
        <td id="L196" class="blob-num js-line-number" data-line-number="196"></td>
        <td id="LC196" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-s1">features</span></td>
      </tr>
      <tr>
        <td id="L197" class="blob-num js-line-number" data-line-number="197"></td>
        <td id="LC197" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L198" class="blob-num js-line-number" data-line-number="198"></td>
        <td id="LC198" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L199" class="blob-num js-line-number" data-line-number="199"></td>
        <td id="LC199" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">model_fn</span>(<span class="pl-s1">model_dir</span>):</td>
      </tr>
      <tr>
        <td id="L200" class="blob-num js-line-number" data-line-number="200"></td>
        <td id="LC200" class="blob-code blob-code-inner js-file-line">    <span class="pl-s">"""Deserialize fitted model"""</span></td>
      </tr>
      <tr>
        <td id="L201" class="blob-num js-line-number" data-line-number="201"></td>
        <td id="LC201" class="blob-code blob-code-inner js-file-line">    <span class="pl-s1">preprocessor</span> <span class="pl-c1">=</span> <span class="pl-s1">joblib</span>.<span class="pl-en">load</span>(<span class="pl-s1">os</span>.<span class="pl-s1">path</span>.<span class="pl-en">join</span>(<span class="pl-s1">model_dir</span>, <span class="pl-s">"model.joblib"</span>))</td>
      </tr>
      <tr>
        <td id="L202" class="blob-num js-line-number" data-line-number="202"></td>
        <td id="LC202" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> <span class="pl-s1">preprocessor</span></td>
      </tr>
</tbody></table>

  <details class="details-reset details-overlay BlobToolbar position-absolute js-file-line-actions dropdown d-none" aria-hidden="true">
    <summary class="btn-octicon ml-0 px-2 p-0 color-bg-primary border color-border-tertiary rounded-1" aria-label="Inline file action toolbar" aria-haspopup="menu" role="button">
      <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-kebab-horizontal">
    <path d="M8 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zM1.5 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zm13 0a1.5 1.5 0 100-3 1.5 1.5 0 000 3z"></path>
</svg>
    </summary>
    <details-menu role="menu">
      <ul class="BlobToolbar-dropdown dropdown-menu dropdown-menu-se mt-2" style="width:185px">
        <li>
          <clipboard-copy role="menuitem" class="dropdown-item" id="js-copy-lines" style="cursor:pointer;" tabindex="0">
            Copy lines
          </clipboard-copy>
        </li>
        <li>
          <clipboard-copy role="menuitem" class="dropdown-item" id="js-copy-permalink" style="cursor:pointer;" tabindex="0">
            Copy permalink
          </clipboard-copy>
        </li>
        <li><a class="dropdown-item js-update-url-with-hash" id="js-view-git-blame" role="menuitem" href="https://github.com/aws/amazon-sagemaker-examples/blame/2e95ceb9f5f6128863d976c9174ecbe2822e444a/sagemaker-python-sdk/scikit_learn_inference_pipeline/sklearn_abalone_featurizer.py">View git blame</a></li>
          <li><a class="dropdown-item" id="js-new-issue" role="menuitem" href="https://github.com/aws/amazon-sagemaker-examples/issues/new">Reference in new issue</a></li>
      </ul>
    </details-menu>
  </details>

  </div>

    </div>


  

  <details class="details-reset details-overlay details-overlay-dark" id="jumpto-line-details-dialog">
    <summary data-hotkey="l" aria-label="Jump to line" role="button"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast linejump" aria-label="Jump to line" role="dialog" aria-modal="true">
      <!-- '"` --><!-- </textarea></xmp> --><form class="js-jump-to-line-form Box-body d-flex" action="https://github.com/aws/amazon-sagemaker-examples/blob/master/sagemaker-python-sdk/scikit_learn_inference_pipeline/sklearn_abalone_featurizer.py" accept-charset="UTF-8" method="get">
        <input class="form-control flex-auto mr-3 linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line…" aria-label="Jump to line" autofocus="">
        <button data-close-dialog="" type="submit" data-view-component="true" class="btn">
  
  Go
  

</button>
</form>    </details-dialog>
  </details>

    <div class="Popover anim-scale-in js-tagsearch-popover" hidden="" data-tagsearch-url="/aws/amazon-sagemaker-examples/find-definition" data-tagsearch-ref="master" data-tagsearch-path="sagemaker-python-sdk/scikit_learn_inference_pipeline/sklearn_abalone_featurizer.py" data-tagsearch-lang="Python" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.click_on_symbol&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;click_on_symbol&quot;,&quot;repository_id&quot;:107937815,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/aws/amazon-sagemaker-examples/blob/master/sagemaker-python-sdk/scikit_learn_inference_pipeline/sklearn_abalone_featurizer.py?_pjax=%23repo-content-pjax-container&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="175cf27760c8ec95c8a6387efbfa79adbc122ce90e18f2fe0631f139bcd6a7ae">
  <div class="Popover-message Popover-message--large Popover-message--top-left TagsearchPopover mt-1 mb-4 mx-auto Box color-shadow-large">
    <div class="TagsearchPopover-content js-tagsearch-popover-content overflow-auto" style="will-change:transform;">
    </div>
  </div>
</div>


</div>















</div>
</div>

    </main>
  </div>

  </div>

          
<div class="footer container-xl width-full p-responsive" role="contentinfo">
  <div class="position-relative d-flex flex-row-reverse flex-lg-row flex-wrap flex-lg-nowrap flex-justify-center flex-lg-justify-between pt-6 pb-2 mt-6 f6 color-text-secondary border-top color-border-secondary ">
    <ul class="list-style-none d-flex flex-wrap col-12 col-lg-5 flex-justify-center flex-lg-justify-between mb-2 mb-lg-0">
      <li class="mr-3 mr-lg-0">© 2021 GitHub, Inc.</li>
        <li class="mr-3 mr-lg-0"><a href="https://docs.github.com/en/github/site-policy/github-terms-of-service" data-ga-click="Footer, go to terms, text:terms">Terms</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://docs.github.com/en/github/site-policy/github-privacy-statement" data-ga-click="Footer, go to privacy, text:privacy">Privacy</a></li>
        <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to security, text:security" href="https://github.com/security">Security</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://www.githubstatus.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
        <li><a data-ga-click="Footer, go to help, text:Docs" href="https://docs.github.com/">Docs</a></li>
    </ul>

    <a aria-label="Homepage" title="GitHub" class="footer-octicon d-none d-lg-block mx-lg-4" href="https://github.com/">
      <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="24" width="24" class="octicon octicon-mark-github">
    <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path>
</svg>
</a>
    <ul class="list-style-none d-flex flex-wrap col-12 col-lg-5 flex-justify-center flex-lg-justify-between mb-2 mb-lg-0">
        <li class="mr-3 mr-lg-0"><a href="https://support.github.com/" data-ga-click="Footer, go to contact, text:contact">Contact GitHub</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://github.com/pricing" data-ga-click="Footer, go to Pricing, text:Pricing">Pricing</a></li>
      <li class="mr-3 mr-lg-0"><a href="https://docs.github.com/" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li class="mr-3 mr-lg-0"><a href="https://services.github.com/" data-ga-click="Footer, go to training, text:training">Training</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://github.blog/" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a data-ga-click="Footer, go to about, text:about" href="https://github.com/about">About</a></li>
    </ul>
  </div>
  <div class="d-flex flex-justify-center pb-6">
    <span class="f6 color-text-tertiary"></span>
  </div>

  
</div>



  <div id="ajax-error-message" class="ajax-error-message flash flash-error" hidden="">
    <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-alert">
    <path fill-rule="evenodd" d="M8.22 1.754a.25.25 0 00-.44 0L1.698 13.132a.25.25 0 00.22.368h12.164a.25.25 0 00.22-.368L8.22 1.754zm-1.763-.707c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0114.082 15H1.918a1.75 1.75 0 01-1.543-2.575L6.457 1.047zM9 11a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.25a.75.75 0 00-1.5 0v2.5a.75.75 0 001.5 0v-2.5z"></path>
</svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-x">
    <path fill-rule="evenodd" d="M3.72 3.72a.75.75 0 011.06 0L8 6.94l3.22-3.22a.75.75 0 111.06 1.06L9.06 8l3.22 3.22a.75.75 0 11-1.06 1.06L8 9.06l-3.22 3.22a.75.75 0 01-1.06-1.06L6.94 8 3.72 4.78a.75.75 0 010-1.06z"></path>
</svg>
    </button>
    You can’t perform that action at this time.
  </div>

  <div class="js-stale-session-flash flash flash-warn flash-banner" hidden="">
    <svg aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" height="16" width="16" class="octicon octicon-alert">
    <path fill-rule="evenodd" d="M8.22 1.754a.25.25 0 00-.44 0L1.698 13.132a.25.25 0 00.22.368h12.164a.25.25 0 00.22-.368L8.22 1.754zm-1.763-.707c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0114.082 15H1.918a1.75 1.75 0 01-1.543-2.575L6.457 1.047zM9 11a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.25a.75.75 0 00-1.5 0v2.5a.75.75 0 001.5 0v-2.5z"></path>
</svg>
    <span class="js-stale-session-flash-signed-in" hidden="">You signed in with another tab or window. <a href="https://github.com/aws/amazon-sagemaker-examples/blob/master/sagemaker-python-sdk/scikit_learn_inference_pipeline/sklearn_abalone_featurizer.py">Reload</a> to refresh your session.</span>
    <span class="js-stale-session-flash-signed-out" hidden="">You signed out in another tab or window. <a href="https://github.com/aws/amazon-sagemaker-examples/blob/master/sagemaker-python-sdk/scikit_learn_inference_pipeline/sklearn_abalone_featurizer.py">Reload</a> to refresh your session.</span>
  </div>
    <template id="site-details-dialog"></template>

    <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none; --darkreader-inline-outline: initial;" tabindex="0" data-darkreader-inline-outline="">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box color-shadow-large" style="width:360px;"></div>
</div>

    <template id="snippet-clipboard-copy-button"></template>



  

  


<div aria-live="polite" class="sr-only">Loading complete</div></body></html>