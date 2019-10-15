# Transaction
use autocommit by default, each query is executed in its own transaction
autocommit may not be a good choice for innodb

_Each query is immediately committed to the database, unless a transaction is active_


# how to install django_wsgiserver with pyopenssl
     pip install pyopenssl==0.13
     pip install django_wsgiserver
   
     cp OpenSSL/SSL.so OpenSSL.SSL.so
     cp OpenSSL/rand.so OpenSSL.rand.so
     cp OpenSSL/crypto.so OpenSSL.crypto.so

# Django n+1 issues
## example
        class ModelF(model):
              name=CharField(max_length=255L, unique=True)
              b=ForeignKey(ModelB, related_name = 'fs')
              c=OneToOneField(ModelC, related_name='f')  
              ds=ManyToManyField(ModelD, related_name='fs')

        class ModelB(model):
              name=CharField(max_length=255L, unique=True)

        class ModelC(model):
              name=CharField(max_length=255L, unique=True)

        class ModelD(model):
              name=CharField(max_length=255L, unique=True)

         
## Forward many to one
        as = ModelA.objects.all()
        for a in as:
            print a.b.name

## reverse many to one
        bs = ModelB.objects.all()
        for b in bs:
            print b.a_set.all()

## forward many to many
        as = ModelA.objects.all()
        for a in as:
            print a.ds.all()

## forward one to one
        as = ModelA.objects.all()
        for a in as:
            print a.c.name
## reverse one to one
        cs = ModelC.objects.all()
        for c in cs:
            print c.a.name
 
     #fs = ModelF.objects.all()
     fs = ModelF.objects.all().select_related('b__name', 'c__name') #.prefetch_related('ds')
     for f in fs:
        # foreignkey
        print f.b.name

        # onetoone
        print f.c.name

        # manytomany
        ds = f.ds.all()
        for d in ds:
            print d.name

    # OneToMany (reverse foreign relation, not work, issue of django 1.6 probably)
    #bs = ModelB.objects.select_related('fs').all()
    #for b in bs:
    #    print b.fs.all()


    ### reverse onetoone, not work, issue of django 1.6 probably)
    ##cs = ModelC.objects.all()
    ##for c in cs:
    ##    print c.f.name

    # reverse many to many
    ds = ModelD.objects.all() #.prefetch_related('fs')
    for d in ds:
        print d.fs.all()


    Potential n+1 query detected on `ModelD.modelf`
