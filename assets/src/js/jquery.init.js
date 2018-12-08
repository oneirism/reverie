var yl = yl || {};

if (yl.jQuery === undefined) {
    /* If the user has included another copy of jQuery use that, even in the admin */
    if (typeof $ !== 'undefined')
        console.log("Dollar is defined.")

        yl.jQuery = $;
}
