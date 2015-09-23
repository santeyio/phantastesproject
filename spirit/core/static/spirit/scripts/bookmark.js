// Generated by CoffeeScript 1.7.1

/*
  A library to tell the server how far you have scrolled down.
  requires: waypoints
 */

(function() {
  var $, Bookmark, Mark,
    __bind = function(fn, me){ return function(){ return fn.apply(me, arguments); }; };

  $ = jQuery;

  Mark = (function() {
    function Mark() {
      this.isSending = false;
      this.commentNumber = this._getCommentNumber();
    }

    Mark.prototype._getCommentNumber = function() {
      var commentNumber;
      commentNumber = window.location.hash.split("#c")[1];
      commentNumber = parseInt(commentNumber, 10);
      if (isNaN(commentNumber)) {
        commentNumber = 0;
      } else {

      }
      commentNumber -= 1;
      return commentNumber;
    };

    return Mark;

  })();

  Bookmark = (function() {
    Bookmark.prototype.defaults = {
      csrfToken: "csrf_token",
      target: "target url"
    };

    function Bookmark(el, mark, options) {
      this.sendCommentNumber = __bind(this.sendCommentNumber, this);
      this.onWaypoint = __bind(this.onWaypoint, this);
      this.el = $(el);
      this.mark = mark;
      this.options = $.extend({}, this.defaults, options);
      this.setUp();
    }

    Bookmark.prototype.setUp = function() {
      return this.el.waypoint(this.onWaypoint, {
        offset: '100%'
      });
    };

    Bookmark.prototype.onWaypoint = function() {
      var newCommentNumber;
      newCommentNumber = this.el.data('number');
      if (newCommentNumber > this.mark.commentNumber) {
        this.mark.commentNumber = newCommentNumber;
        this.sendCommentNumber();
      }
    };

    Bookmark.prototype.sendCommentNumber = function() {
      var post;
      if (this.mark.isSending) {
        return;
      }
      this.mark.isSending = true;
      post = $.post(this.options.target, {
        csrfmiddlewaretoken: this.options.csrfToken,
        comment_number: this.mark.commentNumber
      });
      return post.always((function(_this) {
        return function() {
          return _this.mark.isSending = false;
        };
      })(this));
    };

    return Bookmark;

  })();

  $.fn.extend({
    bookmark: function(options) {
      var mark;
      mark = new Mark();
      return this.each(function() {
        if (!$(this).data('plugin_bookmark')) {
          return $(this).data('plugin_bookmark', new Bookmark(this, mark, options));
        }
      });
    }
  });

  $.fn.bookmark.Bookmark = Bookmark;

  $.fn.bookmark.Mark = Mark;

}).call(this);

//# sourceMappingURL=bookmark.map
