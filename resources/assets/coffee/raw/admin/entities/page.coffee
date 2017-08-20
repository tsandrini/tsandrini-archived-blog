(($) ->

    $(document).on "ready", ->

        $dynamicContentInput = $('#id_dynamic_content')
        $dynamicContentInput.fn = {}

        $dynamicContentInput.on "change", (e) ->
            $dynamicContentInput.fn.change(e)

        $dynamicContentInput.fn.change = (e) ->

            $target = $('[id^=id_content_]').parent().parent().parent()

            if $dynamicContentInput.is ':checked' then $target.fadeIn 300 else $target.fadeOut 300

        # Called on page load
        # Just to group things at one place
        init = () ->
            $dynamicContentInput.fn.change()

)(django.jQuery)
